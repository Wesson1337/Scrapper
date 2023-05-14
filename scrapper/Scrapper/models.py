from scrapy.utils.project import get_project_settings
from sqlalchemy.orm import declarative_base
import sqlalchemy as sa

Base = declarative_base()


def connect_db():
    return sa.create_engine(get_project_settings().get("DB_URL"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Record(Base):
    __tablename__ = "record"

    id = sa.Column(sa.Integer, primary_key=True)
    url = sa.Column(sa.String(255), index=True, nullable=False)
    name = sa.Column(sa.String(255), index=True, nullable=False)
    cd_usd_price = sa.Column(sa.Float, nullable=False)
    vinyl_usd_price = sa.Column(sa.Float, nullable=False)
    release_type = sa.Column(sa.String(255), nullable=False)
    artist = sa.Column(sa.String(255), nullable=False)
    artist_page = sa.Column(sa.String(255), nullable=False)
    genre = sa.Column(sa.String(255), nullable=False)
    release_year = sa.Column(sa.Integer, nullable=True)
    label = sa.Column(sa.String(255), nullable=False)
    country = sa.Column(sa.String(255), nullable=True)
