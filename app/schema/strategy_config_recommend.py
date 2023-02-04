from pydantic import BaseModel

from app.model.stock_strategy_config import StockStrategyConfig
from app.model.stock_strategy_log_2 import StockStrategyLog2
from app.model.stock_strategy_result import StockStrategyResult


class StrategyConfigRecommendSchema(BaseModel):
    stock_code: str
    start_date: str
    end_date: str
    fee_rate: float
    par: list
    iterations: int


class StrategyConfigRecommendRespSchema(BaseModel):
    stock_code: str
    start_date: str
    end_date: str
    params: dict
    fee_rate: float
    profit_rate: float
