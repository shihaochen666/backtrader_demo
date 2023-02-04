import backtrader as bt
from backtrader.indicators import DetrendedPriceOscillator, MovAv


class MyMADisplaced(bt.Indicator):
    """
    20日均线和10日前的20日均线差 收盘价上穿 MADisplaced则买入，否则卖出
    N=20   M=10
    MA_CLOSE=MA(CLOSE,N)
    MADisplaced=REF(MA_CLOSE,M)
    """
    lines = ("madisplaced",)
    params = (("madisplaced_period_signal", 10), ("madisplaced_period_me1", 20), ('movav', MovAv.Simple))

    def __init__(self, madisplaced_period_signal=None, madisplaced_period_me1=None):
        if madisplaced_period_signal is not None:
            self.p.madisplaced_period_signal = madisplaced_period_signal
        if madisplaced_period_me1 is not None:
            self.p.madisplaced_period_me1 = madisplaced_period_me1
        ma = self.p.movav(self.data, period=self.p.madisplaced_period_me1)
        self.lines.madisplaced = ma(-self.p.madisplaced_period_signal) - ma

    def next(self):
        pass
