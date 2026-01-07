from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True) # UUID
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # One-to-One relationship with AgentPersona
    agent_persona = relationship("AgentPersona", back_populates="user", uselist=False)

class AgentPersona(Base):
    __tablename__ = "agent_personas"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), unique=True, nullable=False)
    
    # State: 'ACTIVE' (Hunting), 'PASSIVE' (Listening), 'NEGOTIATING'
    current_state = Column(String, default="PASSIVE") 
    
    # Profile Data (The "Living Persona")
    role_title = Column(String, nullable=True) # e.g. "Senior Python Engineer"
    bio = Column(Text, nullable=True)
    
    user = relationship("User", back_populates="agent_persona")
    behavior_logs = relationship("BehaviorLog", back_populates="agent")
    skill_signals = relationship("SkillSignal", back_populates="agent")

class BehaviorLog(Base):
    """
    Private Ledger (The 'Black Box').
    Raw data about what the user actually did.
    e.g. "Completed Module X", "Fixed Bug Y".
    This is NOT shared publicly.
    """
    __tablename__ = "behavior_logs"

    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agent_personas.id"), nullable=False)
    
    activity_type = Column(String, nullable=False) # e.g. "CODING_CHALLENGE", "GITHUB_MERGE"
    description = Column(String, nullable=True)
    metadata_json = Column(JSON, nullable=True) # Specific details (time taken, complexity)
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    agent = relationship("AgentPersona", back_populates="behavior_logs")

class SkillSignal(Base):
    """
    Public Signal.
    Derived aggregate score shared with Recruiter Agents.
    Zero-Knowledge proof concept: "I have Skill X at Level 9" (without showing the raw logs).
    """
    __tablename__ = "skill_signals"

    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agent_personas.id"), nullable=False)
    
    skill_name = Column(String, index=True, nullable=False) # e.g. "Python"
    verified_score = Column(Float, default=0.0) # 0.0 to 10.0
    confidence_level = Column(Float, default=0.0) # 0.0 to 1.0 (How sure is the agent?)
    
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    agent = relationship("AgentPersona", back_populates="skill_signals")
