import datetime
import random
import backtrader as bt
import numpy as np
import pandas as pd
import gradient_free_optimizers as gfo

from app.dao.strategy import StrategyDao
from app.model.stock_strategy_log_2 import StockStrategyLog2
from app.scheduler.my_strategy_tuning import StrategyUnifiedTuning
from app.schema.strategy_config_recommend import StrategyConfigRecommendSchema, StrategyConfigRecommendRespSchema
from app.utils.dpo_ind import MyDPO
from app.utils.er_ind import MyER
from app.utils.maamt_ind import MyMAAMT
from app.utils.madisplaced_ind import MyMADisplaced
from app.utils.my_pandas_data import MyPandasData
from app.utils.pac_ind import MyPAC
from app.utils.po_ind import MyPO
from app.utils.policy_ind_config import PolicyIndConfig


class StrategyConfigRecommendService:

    def __init__(self, strategy_recommend: StrategyConfigRecommendSchema, db):
        self.strategy_recommend = strategy_recommend
        self.dao = StrategyDao(db)
        self.search_sapce = self.filter_search_sapce(strategy_recommend.par)

    def filter_search_sapce(self, pars):
        search_sapce = {
            "dpo_period": np.arange(1, 30, 1),
            "er_period_me1": np.arange(1, 30, 1),
            "maamt_period_me1": np.arange(1, 30, 1),
            "madisplaced_period_signal": np.arange(1, 30, 1),
            "madisplaced_period_me1": np.arange(1, 30, 1),
            "pac_period_low": np.arange(1, 30, 1),
            "pac_period_high": np.arange(1, 30, 1),
            "po_period_short": np.arange(1, 30, 1),
            "po_period_long": np.arange(1, 30, 1)
        }
        new_search_sapce = {}
        for key, value in search_sapce.items():
            for par in pars:
                if key.startswith(par.lower()):
                    new_search_sapce[key] = np.arange(1, 30, 1)

        return new_search_sapce

    def run(self, par):
        history_info = self.dao.read_by_code_and_date(self.strategy_recommend.stock_code,
                                                      self.strategy_recommend.start_date,
                                                      self.strategy_recommend.end_date)
        close_price, open_price, min_price, max_price, trading_amount, timesimple, collect_date = [], [], [], [], [], [], []
        for info in history_info:
            close_price.append(info.close_price)
            open_price.append(info.open_price)
            min_price.append(info.min_price)
            max_price.append(info.max_price)
            collect_date.append(info.collect_date)
            trading_amount.append(info.trading_amount)
            timesimple.append(datetime.datetime.strptime(info.collect_date, "%Y-%m-%d"))
        dataframe = pd.DataFrame(
            {'close': close_price, 'open': open_price, 'low': min_price, 'high': max_price,
             'amount': trading_amount,
             "datetime": collect_date}, index=timesimple)
        cerebro = bt.Cerebro()
        # Add a strategy
        cerebro.addstrategy(StrategyUnifiedTuning, parline=self.strategy_recommend.par, par=par)
        data = MyPandasData(dataname=dataframe)
        # Add the Data Feed to Cerebro
        cerebro.adddata(data)
        # Set our desired cash start
        cerebro.broker.setcash(1000)
        cerebro.broker.setcommission(self.strategy_recommend.fee_rate)
        cerebro.addsizer(bt.sizers.AllInSizer, percents=95)

        # Print out the starting conditions
        # print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

        # Run over everything
        cerebro.run(maxcpus=4)

        score = cerebro.broker.getvalue()
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        return score

    def bast_score(self):
        # 可以使用的优化器  https://zhuanlan.zhihu.com/p/561632532
        # 创建优化器
        opt = gfo.EvolutionStrategyOptimizer(self.search_sapce)
        opt.search(self.run, n_iter=self.strategy_recommend.iterations)
        print(opt.best_para)
        print(opt.best_score)
        strategy_config_recommend_resp = StrategyConfigRecommendRespSchema()
        strategy_config_recommend_resp.profit_rate = float(opt.best_score / 1000)
        strategy_config_recommend_resp.params = opt.best_para
        strategy_config_recommend_resp.start_date = str(self.strategy_recommend.start_date)
        strategy_config_recommend_resp.end_date = str(self.strategy_recommend.end_date)
        strategy_config_recommend_resp.stock_code = str(self.strategy_recommend.stock_code)
        strategy_config_recommend_resp.fee_rate = float(self.strategy_recommend.fee_rate)
        return strategy_config_recommend_resp


class StrategyUnifiedTuning(bt.Strategy):
    # 默认值 必须给
    params = (
        ("dpo_period", 20),
        ("er_period_me1", 20),
        ("maamt_period_me1", 20),
        ("madisplaced_period_signal", 20), ("madisplaced_period_me1", 20),
        ("pac_period_low", 20), ("pac_period_high", 20),
        ("po_period_short", 20), ("po_period_long", 20),
    )

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self, *args, **kwargs):
        self.trader_log = []
        self.ind_params = kwargs["parline"]
        self.par = kwargs["par"]

        # 绑定对应关系
        # for key, value in ind_name_relation.items():
        #     values = value.split("_")
        #     prefix = values[0]
        #     index = int(values[1])
        # config_params_value = self.ind_params.get(prefix)
        # if config_params_value is not None:
        for key, value in self.par.items():
            setattr(self.p, key, value)
        self.dataclose = self.datas[0].close
        # To keep track of pending orders
        self.order = None
        self.DPO = MyDPO(dpo_period=self.p.dpo_period)
        self.PO = MyPO(po_period_short=self.p.po_period_short, po_period_long=self.p.po_period_long)
        self.PAC = MyPAC(pac_period_low=self.p.pac_period_low, pac_period_high=self.p.pac_period_high)
        self.ER = MyER(er_period_me1=self.p.er_period_me1)
        self.MAAMT = MyMAAMT(maamt_period_me1=self.p.maamt_period_me1)
        self.MADisplaced = MyMADisplaced(madisplaced_period_signal=self.p.madisplaced_period_signal,
                                         madisplaced_period_me1=self.p.madisplaced_period_me1)
        self.pic = PolicyIndConfig()
        self.batch_no = "".join([str(random.randint(0, 10)) for i in range(20)])

    def notify(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enougth cash
        if order.status in [order.Completed, order.Canceled, order.Margin]:
            stock_strategy_log2 = StockStrategyLog2()
            stock_strategy_log2.batch_no = self.batch_no
            stock_strategy_log2.trans_fee = order.executed.comm
            stock_strategy_log2.trans_date = self.datas[0].datetime.date(0).isoformat()
            stock_strategy_log2.mark_price = order.executed.price
            stock_strategy_log2.trans_amount = order.executed.value
            if order.isbuy():
                stock_strategy_log2.trans_type = "buy"
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                stock_strategy_log2.trans_type = "sell"
                self.log('SELL 交易价格, %.2f' % order.executed.price)
                # self.log('SELL 交易数量, %.2f' % order.executed.size)
                # self.log('SELL 交易金额, %.2f' % order.executed.value)
                # self.log('SELL 手续费, %.2f' % order.executed.comm)
            self.trader_log.append(stock_strategy_log2)
            self.bar_executed = len(self)

        # Write down: no pending order
        self.order = None

    def next(self):
        policys = []
        for param in self.ind_params:
            lines = getattr(self, param).lines.__dict__.get("lines")
            policy = getattr(self.pic, param.lower())
            policys.append(policy(lines))
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if policys.count(True) == len(policys):
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()

        else:
            # Already in the market ... we might sell
            if policys.count(False) == len(policys):
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
