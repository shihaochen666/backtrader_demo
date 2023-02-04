import backtrader as bt
from numpy import mean

from app.schema.base_myind import BaseMyInd


class MyDPO(bt.Indicator, BaseMyInd):
    """
    假设N=20,取当天收盘价与 11天前的20日均线差,DPO>0买入,否则卖出
    CLOSE-REF(MA(CLOSE,N),N/2+1)
    """
    lines = ("dpo",)
    params = (("dpo_period", 20),)

    def __init__(self, dpo_period=None):
        if dpo_period is not None:
            self.p.dpo_period = dpo_period
        self.lines.dpo = bt.indicators.DPO(self.data, period=self.p.dpo_period)

    def next(self):
        pass
