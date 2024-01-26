from sqlalchemy import create_engine
from sqlalchemy.orm import create_session


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = create_session(bind=engine)