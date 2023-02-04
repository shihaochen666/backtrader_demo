from fastapi_plus.model.base import *


class StockIndustryRelationConfig(Base):
    __tablename__ = 'stock_industry_relation_config'
    __table_args__ = (
        Index('unq_industry_code', 'stock_industry_id', 'stock_code', unique=True),
        {'comment': '股票所属行业板块关系'}
    )

    id = Column(BigInteger, primary_key=True)
    stock_industry_id = Column(BigInteger, comment='股票所属行业id')
    stock_code = Column(String(255), comment='股票代码')
    stock_join_date = Column(String(20), comment='纳入日期')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
