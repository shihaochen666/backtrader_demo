import backtrader as bt


class MyPO(bt.Indicator):
    """
    长短均线增长速率，短均线大于均线买入否则卖出
    EMA_Short=EMA(CLOSE,9)
    EMA_LONG=EMA(CLOSE,26)
    PO=(EMA_SHORT-EMA_LONG)/EMA_LONG*100
    """
    lines = ("po",)
    params = (("po_period_short", 9), ("po_period_long", 26),)  # 最后一个 “,” 别省略

    def __init__(self, po_period_short=None, po_period_long=None):
        if po_period_short is not None:
            self.p.po_period_short = po_period_short
        if po_period_long is not None:
            self.p.po_period_long = po_period_long
        self.period_short = bt.indicators.EMA(self.data, period=self.p.po_period_short)
        self.period_long = bt.indicators.EMA(self.data, period=self.p.po_period_long)
        self.lines.po = (self.period_short - self.period_long) / self.period_long * 100

    def next(self):
        pass
