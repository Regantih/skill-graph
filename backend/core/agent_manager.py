from uuid import UUID
from backend.core.schemas import AgentPersona, AgentState

class AgentManager:
    def toggle_agent_status(self, agent_id: UUID, target_state: AgentState):
        """
        The 'Ignition Key'.
        User decides when their Digital Twin starts hunting.
        """
        # 1. Fetch Agent from DB (Mocked)
        agent = self._get_agent_by_id(agent_id)
        
        # 2. State Validation
        if agent.state == target_state:
            return {"status": "no_change", "message": f"Agent is already {target_state}"}
            
        # 3. The Switch
        previous_state = agent.state
        agent.state = target_state
        
        # 4. Side Effects (Crucial for CINO narrative)
        if target_state == AgentState.ACTIVE_HUNTING:
            self._broadcast_availability(agent.id) # Pings the Discovery Platform
        elif target_state == AgentState.PASSIVE_LISTENING:
            self._withdraw_signal(agent.id) # Removes from active search
            
        return {"status": "success", "previous": previous_state, "current": agent.state}

    def _broadcast_availability(self, agent_id):
        print(f"📡 AGENT {agent_id} IS NOW LIVE ON THE MARKET.")

    def _withdraw_signal(self, agent_id):
        print(f"🔇 AGENT {agent_id} HAS GONE DARK.")

    def _get_agent_by_id(self, agent_id):
        # Mock DB retrieval for scaffolding
        # In production this queries the `AgentPersona` table
        return AgentPersona(user_id="user_123", state=AgentState.PASSIVE_LISTENING)
