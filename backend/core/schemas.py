from pydantic import BaseModel, Field, validator
from typing import Dict, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

# --- Enums for Strict State Management ---
class AgentState(str, Enum):
    PASSIVE_LISTENING = "PASSIVE_LISTENING"
    ACTIVE_HUNTING = "ACTIVE_HUNTING"
    NEGOTIATING = "NEGOTIATING"
    HIRED = "HIRED"

class IntentType(str, Enum):
    OPEN_TO_WORK = "OPEN_TO_WORK"
    SCOUTING = "SCOUTING"
    LEARNING = "LEARNING"

# --- 1. The SkillSignal (The Public Broadcast Packet) ---
class SkillSignal(BaseModel):
    """
    The 'Verified' Public Identity. 
    This is the ONLY data shared with the outside world.
    Zero-Knowledge Architectue: It reveals the SCORE, not the LOGS.
    """
    agent_id: UUID = Field(..., description="The unique ID of the agent broadcasting this signal.")
    intent: IntentType = Field(..., description="Current strategic goal of the agent.")
    
    # THE VECTOR CORE:
    # Key = Skill Name (e.g., 'Python'), Value = Confidence Score (0.0 to 1.0)
    verified_vectors: Dict[str, float] = Field(
        ..., 
        description="Normalized confidence scores derived from private behavior logs."
    )
    
    # THE VELOCITY METRIC:
    # A multiplier (e.g., 1.0 = normal, 2.5 = accelerated learner)
    learning_velocity: float = Field(
        1.0, 
        ge=0.0, 
        le=10.0, 
        description="The rate at which this agent acquires new vectors."
    )
    
    timestamp: datetime = Field(default_factory=datetime.now)

    @validator('verified_vectors')
    def validate_confidence_scores(cls, v):
        """
        Enforce the 0.0 - 1.0 confidence constraint.
        This prevents 'Grade Inflation' by rogue agents.
        """
        for skill, score in v.items():
            if not (0.0 <= score <= 1.0):
                raise ValueError(f"Skill '{skill}' has invalid confidence score {score}. Must be 0.0-1.0.")
        return v

# --- 2. The AgentPersona (The Digital Twin Config) ---
class AgentPersona(BaseModel):
    """
    The Internal State of the Agent.
    """
    id: UUID = Field(default_factory=uuid4)
    user_id: str  # Link to the human user
    state: AgentState = Field(default=AgentState.PASSIVE_LISTENING)
    
    # Configuration for Autonomy
    configuration: Dict[str, str] = Field(
        default={
            "autonomy_level": "LOW",
            "privacy_setting": "ZERO_KNOWLEDGE_PROOF"
        }
    )
    
    creation_date: datetime = Field(default_factory=datetime.now)

# --- 3. The BehaviorLog (The Private Ledger) ---
class BehaviorLog(BaseModel):
    """
    The Raw Evidence. Stored encrypted. Never shared directly.
    """
    id: UUID = Field(default_factory=uuid4)
    user_id: str
    action_type: str  # e.g., "LEGACY_IMPORT", "GITHUB_COMMIT", "COURSE_COMPLETION"
    details: str
    
    # The weight of this action (0.0 to 1.0)
    impact_score: float = Field(..., ge=0.0, le=1.0)
    
    timestamp: datetime = Field(default_factory=datetime.now)
