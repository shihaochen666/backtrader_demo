from fastapi_plus.model.base import *


class StockStrategyLog(Base):
    __tablename__ = 'stock_strategy_log'
    __table_args__ = {'comment': '策略'}

    id = Column(BigInteger, primary_key=True)
    strategy_name = Column(String(255), comment='策略名字')
    strategy_desc = Column(String(2000), comment='策略描述')
    strategy_formula = Column(String(2000), comment='公式')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='状态0正常1删除')
