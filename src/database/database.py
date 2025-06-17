from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from settings.database_config import folhaPonto
import os

if(not os.path.exists("./src/data")):
    os.makedirs("./src/data")

# engine = create_engine(str(folhaPonto.DATABASE_URL+folhaPonto.PATH_DATABASE+folhaPonto.DATABASE))
engine = create_engine("sqlite:///src/data/registro_Ponto.db")
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base()