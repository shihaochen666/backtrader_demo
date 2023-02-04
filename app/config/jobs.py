from app.main import scheduler
from app.scheduler.my_strategy import MyStrategy

scheduler.add_job(MyStrategy().run, 'interval', seconds=5, id="strategy_job")
