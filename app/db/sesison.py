from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


from app.core.config import db_settings


engine = create_engine(db_settings.POSTGRES_SERVER, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
