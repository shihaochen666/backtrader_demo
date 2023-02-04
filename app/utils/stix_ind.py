import backtrader as bt
from numpy import mean

from app.schema.base_myind import BaseMyInd


class MySTIX(bt.Indicator, BaseMyInd):
    """
    上涨股票个数占总股票个数的比例的移动平均值,上穿50买入，否则卖出
    STIX=EMA(UP_STOCK/(UP_STOCK+DOWN_STOCK)*100,N)
    """
    lines = ("stix",)
    params = (("period_me1", 20), ("period_signal", 1))  # 最后一个 “,” 别省略

    def __init__(self):
        pass

    def next(self):
        pass
