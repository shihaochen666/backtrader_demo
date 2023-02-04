import backtrader as bt


class MyMAAMT(bt.Indicator):
    """
    成交额移动平均线，成交额大于MAAMT则买入，否则卖出
    N=40  MAAMT=MA(AMOUNT,N)
    """
    lines = ("maamt",)
    params = (("maamt_period_me1", 20),)

    def __init__(self, maamt_period_me1=None):
        if maamt_period_me1 is not None:
            self.p.maamt_period_me1 = maamt_period_me1
        self.me1 = bt.indicators.MovingAverageSimple(self.data.amount, period=self.p.maamt_period_me1)
        self.lines.maamt = self.data.amount[0] - self.me1

    def next(self):
        pass
