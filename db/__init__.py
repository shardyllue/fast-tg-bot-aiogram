from utils.config import PG_URL

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker, AsyncSession
)



engine = create_async_engine(
    url="postgresql+asyncpg://" + PG_URL
)

Session = async_sessionmaker(
    bind=engine, 
    expire_on_commit=True
)