import json
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from .config.db import SessionLocal
from .config.fastapi import FastapiConfig
from .controller.api_v1 import api_v1_router

app = FastAPI(**FastapiConfig.__dict__)
app.include_router(api_v1_router, prefix='/v1')

# 创建一个依赖
# def get_db():
#     """每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


interval_task = {
    # 配置存储器
    # "jobstores": {
    #     # 使用Redis进行存储
    #     'default': RedisJobStore(**REDIS_DB)
    # },
    # 配置执行器
    "executors": {
        'default': {'type': 'threadpool', 'max_workers': 20},  # 最大工作线程数20
    },
    # 创建job时的默认参数
    "job_defaults": {
        'coalesce': False,  # 是否合并执行
        'max_instances': 3  # 最大实例数
    }

}

scheduler = AsyncIOScheduler(**interval_task)


@app.on_event("startup")
async def start_event():
    scheduler.start()
    print("定时任务启动成功")


from app.config.jobs import *
