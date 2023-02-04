from fastapi_plus.model.base import *


class XueqiuCombinationList(Base):
    __tablename__ = 'xueqiu_combination_list'
    __table_args__ = {'comment': '雪球组合列表'}

    id = Column(BigInteger, primary_key=True)
    combination_id = Column(Integer, comment='组合id')
    combination_name = Column(String(255), comment='组合名称')
    net_worth = Column(String(255), comment='净值')
    total_income = Column(String(255), comment='总收益')
    user_id = Column(Integer, comment='归属用户id')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间')
    is_deleted = Column(TINYINT, comment='是否删除0正常1删除')
