from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

engine = create_engine("mysql+pymysql://avnadmin:AVNS_w0sWHhp0TXEdxQEYUBQ@mysql-132a0442-jorgeballesterossena-dfbf.h.aivencloud.com:13241/defaultdb?charset=utf8mb4")

connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadata.bind = engine
