from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: UUID
    global_reputation_score: float
    reputation_stake_balance: int

    class Config:
        from_attributes = True
