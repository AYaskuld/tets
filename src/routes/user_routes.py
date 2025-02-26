from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from src.models.users import Users
from src.database.client import get_db
from src.schemas.users import UserCreate, UserResponse

import time
import random


router = APIRouter(tags=["Users"])

@router.get("/getuser", response_model=UserResponse)
async def get_user(name: str, db: AsyncSession = Depends(get_db)):
    user = await db.scalar(select(Users).filter(Users.name == name, Users.deleted_at.is_(None)))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/createuser", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users).filter(Users.name == user_data.name, Users.deleted_at == None))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail=f"User {user_data.name} already exists")

    new_user = Users(name=user_data.name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.delete("/deleteuser", response_model=UserResponse)
async def delete_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users).filter(Users.name == user_data.name, Users.deleted_at == None))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.deleted_at = datetime.now().replace(tzinfo=None)
    await db.commit()
    await db.refresh(user)
    return user


start_time = time.time()
failure_start_time = None

healthy_duration = random.randint(60, 180)
failure_duration = random.randint(60, 180) 

def is_healthy():
    global failure_start_time, start_time, healthy_duration, failure_duration

    current_time = time.time()

    if failure_start_time and (current_time - failure_start_time < failure_duration):
        return False  

    if failure_start_time and (current_time - failure_start_time >= failure_duration):
        failure_start_time = None
        start_time = current_time  
        healthy_duration = random.randint(60, 180)

    if not failure_start_time and (current_time - start_time >= healthy_duration):
        failure_start_time = current_time
        failure_duration = random.randint(60, 180)
        return False

    return True


@router.get("/health")
async def health():
    if is_healthy():
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=503, detail="Service Unavailable")


