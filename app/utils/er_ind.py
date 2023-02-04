import backtrader as bt


class MyER(bt.Indicator):
    """
    假设N=20,当天最高价减去20日均价 且  最低价减去20日均价 都>0买入  都<0则卖出
    BullPower=HIGH-EMA(CLOSE,N)
    BearPower=LOW-EMA(CLOSE,N)
    """
    lines = ("er_bull", "er_bear")
    params = (("er_period_me1", 20),)

    def __init__(self, er_period_me1=None):
        if er_period_me1 is not None:
            self.p.er_period_me1 = er_period_me1
        self.me1 = bt.indicators.EMA(self.data, period=self.p.er_period_me1)
        self.lines.er_bull = self.data.high[0] - self.me1
        self.lines.er_bear = self.data.low[0] - self.me1

    def next(self):
        pass
