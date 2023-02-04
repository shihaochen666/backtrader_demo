from fastapi_plus.model.base import *


class StockConfigList(Base):
    __tablename__ = 'stock_config_list'
    __table_args__ = {'comment': '股票集合'}

    id = Column(BigInteger, primary_key=True)
    stock_code = Column(String(255), comment='股票名称')
    stock_prefix = Column(String(255), comment='前缀')
    stock_name = Column(String(255), comment='股票代码')
    stock_ipo_date = Column(Date, comment='上市日期')
    stock_state = Column(TINYINT, comment='股票状态0正常1停牌2退市')
    stock_price_collect_date = Column(Date, comment='历史股价同步收集时间')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
