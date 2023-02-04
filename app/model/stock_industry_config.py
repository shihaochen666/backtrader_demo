from fastapi_plus.model.base import *


class StockIndustryConfig(Base):
    __tablename__ = 'stock_industry_config'
    __table_args__ = {'comment': '股票行业板块'}

    id = Column(BigInteger, primary_key=True)
    stock_industry = Column(VARCHAR(255), comment='股票所属行业')
    industry_type = Column(String(255), comment='行业分类old,new 两种接口')
    stock_industry_code = Column(String(255), comment='行业code')
    buy_stock_code = Column(String(255), comment='etf代码')
    sync_date = Column(Date, comment='关联关系同步日期')
    stock_industry_factor_date = Column(Date, comment='因子同步日期')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
