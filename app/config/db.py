# 配置文件：DbConfig

from fastapi_plus.utils.db import DbConfig
from sqlalchemy import BigInteger, Column, VARCHAR, DECIMAL, DateTime, Index
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import String, Column, Integer, Float, DateTime, func

db_host = '121.5.145.53'
db_port = '3306'
db_username = 'pig'
db_password = 'ThreePigs3!!BDPig'
db_database = 'pig_data'
db_echo = False

mysql_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}?charset=utf8"
engine = create_engine(
    mysql_url,
    echo=db_echo,
    isolation_level="READ UNCOMMITTED"
    # SQLALCHEMY_DATABASE_URL,
    # connect_args 参数只有sqlite才有
    # connect_args = {
    #     "check_same_thread": False
    # }
)

# 该类的每个实例都是一个数据库会话，该类本身还不是数据库会话，但是一旦我们创建了SessionLocal的实例，这个实例将是实际的数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# 创建数据库基类
Base = declarative_base()
db_config = DbConfig()

db_config.host = '121.5.145.53'
db_config.port = '3306'
db_config.username = 'pig'
db_config.password = 'ThreePigs3!!BDPig'
db_config.database = 'pig_data'
db_config.echo = True


def get_db():
    """每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
