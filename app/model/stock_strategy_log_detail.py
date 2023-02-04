from fastapi_plus.model.base import *


class StockStrategyLogDetail(Base):
    __tablename__ = 'stock_strategy_log_detail'
    __table_args__ = {'comment': '回测记录'}

    id = Column(BigInteger, primary_key=True)
    strategy_log_id = Column(BigInteger, comment='策略id')
    param = Column(String(1000), comment='参数')
    stock_code = Column(String(255), comment='代码')
    start_date = Column(DateTime, comment='开始时间')
    end_date = Column(DateTime, comment='结束时间')
    transaction_count = Column(Integer, comment='交易次数')
    annualized_rate = Column(DECIMAL(20, 8), comment='年化')
    retracement = Column(DECIMAL(20, 8), comment='回撤')
    create_date = Column(DateTime, comment='创建时间')
    is_deleted = Column(TINYINT, comment='状态0正常1删除')
    winning_percentage = Column(DECIMAL(20, 8), comment='胜率')
