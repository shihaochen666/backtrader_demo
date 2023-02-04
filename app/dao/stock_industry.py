from fastapi_plus.dao.base import BaseDao

from app.model.stock_history_price_list import StockHistoryPriceList


class StockIndustryDao(BaseDao):
    def read_by_code_and_date(self, stock_code: str, start_date: str, end_date: str) -> StockHistoryPriceList:
        return self.db.sess.query(StockHistoryPriceList).filter(
            StockHistoryPriceList.stock_code == stock_code,
            StockHistoryPriceList.collect_date >= start_date,
            StockHistoryPriceList.collect_date <= end_date,
            StockHistoryPriceList.is_deleted == 0,
        ).all()
