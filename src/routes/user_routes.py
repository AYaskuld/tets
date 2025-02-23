from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timezone

from src.models.user import User
from src.database.client import get_db
from src.schemas.users import UserCreate, UserResponse

router = APIRouter(prefix="/api", tags=["Users"])

# Получение пользователя
@router.get("/getuser", response_model=UserResponse)
async def get_user(name: str, db: AsyncSession = Depends(get_db)):
    user = await db.scalar(select(User).filter(User.name == name, User.deleted_at.is_(None)))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/createuser", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.name == user_data.name, User.deleted_at == None))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail=f"User {user_data.name} already exists")

    new_user = User(name=user_data.name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.delete("/deleteuser", response_model=UserResponse)
async def delete_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.name == user_data.name, User.deleted_at == None))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.deleted_at = datetime.now().replace(tzinfo=None)
    await db.commit()
    await db.refresh(user)
    return user

@router.get("/health")
async def health():
    return {"message": "Ok"}
