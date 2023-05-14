from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import sqlalchemy as sa
from . import config
from .models import Record
from .dependencies import get_async_session

app = FastAPI()


@app.get(f'{config.API_PREFIX_V1}/records/', response_model=list[Record])
async def get_records(
    session: AsyncSession = Depends(get_async_session)
) -> list[Record]:
    response = await session.execute(sa.select(Record))
    return response.scalars().all()
