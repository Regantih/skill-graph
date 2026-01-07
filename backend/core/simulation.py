import time
import random
from backend.core.schemas import SkillSignal, IntentType

class AgentNegotiationSim:
    def __init__(self):
        print("🤖 INITIALIZING AGENT NEGOTIATION PROTOCOL...\n")

    def run_handshake(self, hiring_agent: SkillSignal, recruiter_reqs: dict):
        """
        Simulates the interaction between Recruiting Agent (RA) and Hiring Agent (HA).
        """
        print(f"[RA] Broadcasting Scout Signal: Looking for {recruiter_reqs['skill']} > {recruiter_reqs['min_score']}")
        time.sleep(1)

        # 1. Match Discovery
        if hiring_agent.verified_vectors.get(recruiter_reqs['skill'], 0) >= recruiter_reqs['min_score']:
            print(f"[MARKET] 🟢 MATCH FOUND: Agent {hiring_agent.agent_id} (Score: {hiring_agent.verified_vectors[recruiter_reqs['skill']]})")
        else:
            print("[MARKET] 🔴 NO MATCH. Terminating.")
            return

        # 2. The Challenge (Verification)
        print("\n[RA] Initiating Challenge: 'Verify Learning Velocity'")
        time.sleep(1)
        
        velocity = hiring_agent.learning_velocity
        print(f"[HA] Retorting: Velocity is {velocity} (High Acceleration)")

        # 3. The Handshake
        if velocity >= recruiter_reqs['min_velocity']:
            print("\n[RA] ✅ CRITERIA MET. HANDSHAKE INITIATED.")
            self._trigger_human_intervention()
        else:
            print("\n[RA] ⚠️ Velocity too low for 'Innovation Squad'. Pass.")

    def _trigger_human_intervention(self):
        print("   >>> 📧 Sending Calendar Invites to Humans...")
        print("   >>> 🔗 Generating Zero-Knowledge Proof Link...")
        print("   >>> 🏁 NEGOTIATION COMPLETE. SUCCESS.")

# Run Simulation
if __name__ == "__main__":
    import uuid
    # Mock Data
    candidate = SkillSignal(
        agent_id=uuid.uuid4(),
        intent=IntentType.OPEN_TO_WORK,
        verified_vectors={"Python": 0.9, "System Design": 0.8},
        learning_velocity=2.5 # Very high
    )
    
    requirements = {"skill": "Python", "min_score": 0.8, "min_velocity": 2.0}
    
    sim = AgentNegotiationSim()
    sim.run_handshake(candidate, requirements)
