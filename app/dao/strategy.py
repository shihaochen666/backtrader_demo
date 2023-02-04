from app.config.db import get_db
from app.model.stock_history_price_list import StockHistoryPriceList
from app.model.stock_strategy_config import StockStrategyConfig
from app.model.stock_strategy_log_2 import StockStrategyLog2


class StrategyDao():
    def __init__(self, db=None):
        if db is None:
            self.db = get_db().__next__()
        else:
            self.db = db

    def read_by_code_and_date(self, stock_code: str, start_date: str, end_date: str) -> StockHistoryPriceList:
        return self.db.query(StockHistoryPriceList).filter(
            StockHistoryPriceList.stock_code == stock_code,
            StockHistoryPriceList.collect_date >= start_date,
            StockHistoryPriceList.collect_date <= end_date,
            StockHistoryPriceList.is_deleted == 0,
        ).order_by(StockHistoryPriceList.collect_date).all()

    def read_config_by_status(self) -> StockStrategyConfig:
        return self.db.query(StockStrategyConfig).filter(
            StockStrategyConfig.status == "I", StockStrategyConfig.is_deleted == 0
        ).all()

    def all_save_log(self, lines: list[StockStrategyLog2]):
        self.db.add_all(lines)
        self.db.commit()

    def update_config(self, id, batch_no, final_capital):
        self.db.query(StockStrategyConfig).filter_by(id=id).update({
            "status": "S", "batch_no": batch_no, "final_capital": final_capital
        })
        self.db.commit()
