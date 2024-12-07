from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import settings


engine = create_engine(settings.app.DB_URL)
Session = sessionmaker(bind=engine)