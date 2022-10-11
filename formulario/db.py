from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE__URL = "postgresql://isisuser:csi20152@192.168.0.45:5432/isis"
engine = create_engine(DATABASE__URL)
sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base  = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()