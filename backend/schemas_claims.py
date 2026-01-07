from pydantic import BaseModel, HttpUrl
from uuid import UUID
from typing import Optional, List

class ClaimBase(BaseModel):
    skill_name: str
    evidence_url: Optional[HttpUrl] = None
    description: Optional[str] = None

class ClaimCreate(ClaimBase):
    user_id: UUID

class Claim(ClaimBase):
    id: UUID
    status: str  # PENDING, VERIFIED, REJECTED
    verification_score: float

    class Config:
        from_attributes = True
