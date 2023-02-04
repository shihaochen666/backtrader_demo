from fastapi_plus.model.base import *


class BuyFundLog(Base):
    __tablename__ = 'buy_fund_log'
    __table_args__ = {'comment': '购买基金记录'}

    id = Column(BigInteger, primary_key=True)
    stock_code = Column(String(255), index=True, comment='购买基金code')
    collect_date = Column(Date, comment='日期')
    current_price = Column(DECIMAL(10, 4), comment='当前基金价格')
    buy_amount = Column(DECIMAL(10, 4), comment='投资金额')
    cash_amount = Column(DECIMAL(10, 4), comment='现金金额')
    fee = Column(DECIMAL(10, 4), comment='手续费')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='状态0正常1删除')
