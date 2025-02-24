from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from datetime import datetime, timezone
from typing import Optional

from src.config.server import DB_Config


engine = create_async_engine(DB_Config.DATABASE_URI, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(nullable=True)