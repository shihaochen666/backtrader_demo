import backtrader as bt


class MyPAC(bt.Indicator):
    """
    最高价和最低价的移动平均构造上轨和下轨,突破上轨做多,突破下轨做空
    N1=20 N2=20
    UPPER=SMA(HIGH,N1,1)
    LOWER=SMA(LOW,N2,1)
    """
    lines = ("pac_period_low", "pac_period_high", "close")
    params = (("pac_period_low", 20), ("pac_period_high", 20))

    def __init__(self, pac_period_low=None, pac_period_high=None):
        if pac_period_low is not None:
            self.p.pac_period_low = pac_period_low
        if pac_period_high is not None:
            self.p.pac_period_low = pac_period_high
        self.lines.pac_period_low = bt.indicators.SMA(self.data.low, period=self.p.pac_period_low)
        self.lines.pac_period_high = bt.indicators.SMA(self.data.high, period=self.p.pac_period_high)
        self.lines.close = self.data.close

    def next(self):
        pass
