from sqlalchemy import Column, Integer, String, Float, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    username = Column(String, unique=True, index=True)
    global_reputation_score = Column(Float, default=0.0)
    reputation_stake_balance = Column(Integer, default=100)
    
    # Note: Relationships like 'verified_by' are stored in the Graph, not here.
