from fastapi_plus.model.base import *


class StockIndustryFactor(Base):
    __tablename__ = 'stock_industry_factor'
    __table_args__ = (
        Index('idx_date_industry', 'industry_id', 'collect_date', unique=True),
        {'comment': '行业指标因子'}
    )

    id = Column(BigInteger, primary_key=True)
    industry_id = Column(BigInteger, comment='行业id')
    collect_date = Column(Date, index=True, comment='收集日期')
    index_factor = Column(DECIMAL(8, 2), comment='指标因子')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
