from fastapi_plus.model.base import *


class StockStrategyResult(Base):
    __tablename__ = 'stock_strategy_result'

    id = Column(Integer, primary_key=True)
    bacth_no = Column(String(255), comment='批次号')
    trans_count = Column(Integer, comment='交易次数')
    close_count = Column(Integer, comment='关单次数')
    win_rate = Column(Float, comment='胜率')
    annualization_rate = Column(Float, nullable=False, comment='年化率')
    max_withdrawal = Column(String(255), comment='最大回撤')
    detail_info = Column(String(255), comment='更多详细数据')
    create_date = Column(DateTime, comment='创建时间', default=func.now())
    update_date = Column(DateTime, comment='更新时间', default=func.now(), onupdate=func.now())
