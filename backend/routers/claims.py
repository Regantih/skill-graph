from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas_claims
from uuid import UUID

router = APIRouter(
    prefix="/claims",
    tags=["claims"],
)

from ..agents.verifier import verifier_agent
from ..graph import GraphService
from ..database import SessionLocal

async def trigger_verification_agent(claim_id: UUID, evidence_url: str):
    print(f"Triggering verification for claim {claim_id} with evidence {evidence_url}")
    result = await verifier_agent.analyze_repo(evidence_url)
    print(f"Agent Result for {claim_id}: {result}")
    
    if result["status"] == "APPROVED":
        # New: Trigger Peer Routing
        db = SessionLocal()
        try:
            graph_service = GraphService(db)
            # Assuming 'Python' is the skill for now, implied from repo analysis
            verifiers = graph_service.find_verifier_for_skill("Python")
            print(f"Identified Verifiers: {verifiers}")
            # TODO: Create notification/task for human verifiers
        finally:
            db.close()

@router.post("/", response_model=schemas_claims.Claim)
def submit_claim(claim: schemas_claims.ClaimCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # Mock Claim Creation - specific logic would go to CRUD
    # For now, return a mock response to unblock frontend dev
    
    mock_claim = schemas_claims.Claim(
        id=UUID("00000000-0000-0000-0000-000000000000"), # Mock ID
        skill_name=claim.skill_name,
        evidence_url=claim.evidence_url,
        description=claim.description,
        status="PENDING",
        verification_score=0.0
    )
    
    if claim.evidence_url:
        background_tasks.add_task(trigger_verification_agent, mock_claim.id, str(claim.evidence_url))
        
    return mock_claim

@router.get("/{user_id}", response_model=list[schemas_claims.Claim])
def get_user_claims(user_id: UUID, db: Session = Depends(get_db)):
    return [] # Empty list for now
