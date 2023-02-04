from app.config.db import *


class StockStrategyLog2(Base):
    __tablename__ = 'stock_strategy_log_2'

    id = Column('id', Integer, primary_key=True)
    batch_no = Column('batch_no', String(255), comment='批次号')
    trans_type = Column('trans_type', String(255), comment='交易类型 sell卖   buy买')
    trans_date = Column('trans_date', String(255), comment='交易日期')
    mark_price = Column('mark_price', Float, comment='标记价格')
    trans_amount = Column('trans_amount', Float, comment='交易金额')
    trans_size = Column('trans_size', Float, comment='交易数量')
    trans_fee = Column('trans_fee', Float, comment='手续费')
    create_date = Column('create_date', DateTime(timezone=True), nullable=False, comment='创建时间',
                         default=func.now())
    update_date = Column('update_date', DateTime(timezone=True), nullable=False, comment='更新时间',
                         default=func.now(), onupdate=func.now())
