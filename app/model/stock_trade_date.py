from fastapi_plus.model.base import *


class StockTradeDate(Base):
    __tablename__ = 'stock_trade_date'
    __table_args__ = {'comment': '交易日'}

    id = Column(BigInteger, primary_key=True)
    trade_day = Column(Date, unique=True, comment='交易日')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
