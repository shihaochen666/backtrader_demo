from fastapi import Depends, APIRouter

from app.config.db import get_db
from app.schema.strategy_config_recommend import StrategyConfigRecommendSchema
from app.service.strategy_config_recommend_service import StrategyConfigRecommendService

router = APIRouter()


@router.post("/recommend", tags=["strategy"], summary="推荐最佳参数")
async def recommend(*, info: StrategyConfigRecommendSchema, db=Depends(get_db)):
    """
    获取推荐参数
    :param : StrategyConfigRecommendSchema
    :return: 推荐参数
    """
    return StrategyConfigRecommendService(info, db).bast_score()
