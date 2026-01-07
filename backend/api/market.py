from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Dict
from backend.core.schemas import SkillSignal

router = APIRouter()

# Mock Database: In production, this is a Vector DB (Pinecone/Weaviate)
# We store 'SkillSignal' objects here.
ACTIVE_MARKET_DB: List[SkillSignal] = []

@router.post("/market/publish")
async def broadcast_signal(signal: SkillSignal):
    """
    Agent pushes their latest Verified Signal to the market.
    """
    # Remove existing signal for this agent to avoid duplicates
    global ACTIVE_MARKET_DB
    ACTIVE_MARKET_DB = [s for s in ACTIVE_MARKET_DB if s.agent_id != signal.agent_id]
    
    ACTIVE_MARKET_DB.append(signal)
    return {"status": "broadcast_active", "market_size": len(ACTIVE_MARKET_DB)}

@router.get("/market/scout", response_model=List[SkillSignal])
async def scout_talent(
    required_skill: str = Query(..., description="The primary vector to search for (e.g. 'Python')"),
    min_confidence: float = Query(0.7, description="Minimum Verified Score (0.0 - 1.0)"),
    min_velocity: Optional[float] = Query(None, description="Minimum Learning Velocity (Find 'Fast Learners')")
):
    """
    The Headhunter Endpoint.
    Recruiting Agents poll this to find candidates.
    """
    matches = []
    
    for signal in ACTIVE_MARKET_DB:
        # 1. Vector Existence Check
        if required_skill not in signal.verified_vectors:
            continue
            
        # 2. Trust Score Check (The "Aggregator" Result)
        agent_score = signal.verified_vectors[required_skill]
        if agent_score < min_confidence:
            continue
            
        # 3. Innovation Check (Velocity)
        # If the recruiter wants a "Fast Learner" (Velocity > 2.0), filter here.
        if min_velocity and signal.learning_velocity < min_velocity:
            continue
            
        matches.append(signal)
    
    return matches
