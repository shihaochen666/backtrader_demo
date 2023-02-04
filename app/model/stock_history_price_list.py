from fastapi_plus.model.base import *


class StockHistoryPriceList(Base):
    __tablename__ = 'stock_history_price_list'
    __table_args__ = (
        Index('unq_collect_date_stock_code', 'stock_code', 'collect_date', unique=True),
        {'comment': '股票历史价格'}
    )

    id = Column(BigInteger, primary_key=True)
    stock_code = Column(VARCHAR(255), index=True, comment='股票代码')
    collect_date = Column(VARCHAR(255), index=True, comment='日期')
    close_price = Column(DECIMAL(20, 4), comment='股票收盘价格')
    open_price = Column(DECIMAL(20, 4), comment='开盘价格')
    min_price = Column(DECIMAL(20, 4), comment='最低价')
    max_price = Column(DECIMAL(20, 4), comment='最高')
    trading_volume = Column(DECIMAL(32, 4), comment='成交量（手）')
    trading_amount = Column(DECIMAL(32, 4), comment='成交额（万）')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
