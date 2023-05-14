from typing import Optional

import sqlmodel as sm
from pydantic import constr
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from . import config


class Record(sm.SQLModel, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    url: constr(max_length=255) = sm.Field(index=True, nullable=False)
    name: constr(max_length=255) = sm.Field(index=True, nullable=False)
    cd_usd_price: float = sm.Field(nullable=False)
    vinyl_usd_price: float = sm.Field(nullable=False)
    release_type: constr(max_length=255) = sm.Field(nullable=False)
    artist: constr(max_length=255) = sm.Field(nullable=False)
    artist_page: constr(max_length=255) = sm.Field(nullable=False)
    genre: constr(max_length=255) = sm.Field(nullable=False)
    release_year: Optional[int] = sm.Field(nullable=True)
    label: constr(max_length=255) = sm.Field(nullable=False)
    country: Optional[constr(max_length=255)] = sm.Field(nullable=True)


engine = create_async_engine(
    config.DB_URL
)

async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


