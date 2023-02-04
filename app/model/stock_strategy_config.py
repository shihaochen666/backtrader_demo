from fastapi_plus.model.base import *


class StockStrategyConfig(Base):
    __tablename__ = 'stock_strategy_config'

    id = Column(Integer, primary_key=True)
    stock_code = Column(VARCHAR(255), nullable=False, comment='股票代码')
    start_date = Column(VARCHAR(255), nullable=False, comment='回测开始时间')
    end_date = Column(VARCHAR(255), nullable=False, comment='回测结束时间')
    batch_no = Column(VARCHAR(255), comment='批次号')
    status = Column(VARCHAR(255), comment='回测状态 I:初始化  P:进行中  F:失败  S:成功')
    params = Column(LONGTEXT, nullable=False,
                    comment="回测参数\\r\\n{\\r\\n'DPO':[x天均线],\\r\\n'ER':[x天均线],\\r\\n'PO':[x天短线,Y天长线],\\r\\n'MAAMT':[x天移动平均线],\\r\\n'MADisplaced':[x天均线,y天前],\\r\\n'PAC':[x天最低平均线，y天最高平均线]\\r\\n}")
    fee_rate = Column(Float, comment='手续费率')
    init_capital = Column(Float, comment='初始资金')
    final_capital = Column(Float, comment='最终资金')
    create_date = Column(DateTime, comment='创建时间')
    update_date = Column(DateTime, comment='更新时间', default=func.now(), onupdate=func.now())
    is_deleted = Column(TINYINT(1), comment='是否删除0正常1删除')
