from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings
from datetime import datetime

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

# Association Table for Many-to-Many relationship between Quote and Tag
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many

class dejobsbase(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    crawled_date = Column(DateTime(), default=datetime.now)
    url = Column('url', Text())
    job_title = Column('job_title', Text())
    company_name = Column('company_name', Text())
    job_description = Column('job_description', Text())
    location = Column('location', Text())
    country = Column('country', Text())
    date_posted = Column('date_posted', Text())




