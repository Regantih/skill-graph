import os
from typing import List, Dict, Any
from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

# --- 1. Define the Extraction Schema (What we want from the LLM) ---
class ExtractedSkill(BaseModel):
    name: str = Field(description="The canonical name of the skill (e.g., 'Python' not 'Python 3.8')")
    years_experience: float = Field(description="Inferred years of experience based on dates or explicit mentions")
    context: str = Field(description="Where this skill was used (e.g., 'Backend API', 'Data Analysis')")

class ResumeData(BaseModel):
    skills: List[ExtractedSkill]
    intent: str = Field(description="The candidate's likely goal: OPEN_TO_WORK, EXPLORING, or CONTRACTING")
    learning_velocity_indicator: float = Field(description="A score 1-10 indicating how quickly they learn new tech based on their history")

class AgentBootstrapper:
    """
    The Conversion Engine: Transforms static text into a living Agent Persona.
    Uses LangChain to parse the resume text into structured data.
    """
    
    def __init__(self, llm_client=None):
        # Initialize the LLM (Ensure OPENAI_API_KEY is in your .env)
        # Using gpt-4-turbo as requested for high-quality extraction
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
        else:
            self.llm = None
            print("WARNING: No OPENAI_API_KEY found. AgentBootstrapper running in MOCK mode.")
        
        # Setup the Parser
        self.parser = PydanticOutputParser(pydantic_object=ResumeData)

    def bootstrap_agent(self, user_id: str, resume_text: str) -> Dict[str, Any]:
        """
        Main entry point. Orchestrates the parsing and instantiation.
        """
        # 1. Extraction: Convert unstructured text to structured JSON
        extracted_data = self._extract_skills_and_intent(resume_text)

        # 2. Instantiation: Create the Digital Twin (Persona)
        persona = self._create_persona(user_id, extracted_data)

        # 3. Seeding: Generate the initial public signal (The "Resume Value")
        signal = self._generate_initial_signal(persona['id'], extracted_data)

        # 4. History: Backfill the private ledger (Legacy data)
        logs = self._backfill_behavior_log(user_id, extracted_data)

        return {
            "persona": persona,
            "signal": signal,
            "initial_logs": logs
        }

    def _extract_skills_and_intent(self, resume_text: str) -> dict:
        """
        Real LangChain Implementation:
        Pipes the resume text through a rigorous extraction prompt.
        """
        if not self.llm:
             # Fallback Mock
            return {
                "extracted_skills": [
                    {"name": "Python", "years": 5, "context": "Backend API (Mock)"},
                ],
                "inferred_intent": "OPEN_TO_WORK",
                "detected_velocity": 1.0
            }

        # 2. The Prompt Template
        prompt = PromptTemplate(
            template="""
            You are an Expert AI Recruiter and Data Scientist.
            Analyze the following resume text and extract structured data.
            
            CRITICAL INSTRUCTION:
            - Normalize skill names (e.g., 'ReactJS' -> 'React').
            - Infer 'learning_velocity_indicator' (1-10) by looking for rapid promotions or learning new stacks quickly.
            
            RESUME TEXT:
            {resume_text}
            
            {format_instructions}
            """,
            input_variables=["resume_text"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()},
        )

        # 3. Execution Chain
        chain = prompt | self.llm | self.parser
        
        try:
            # Execute and get Pydantic object back
            result: ResumeData = chain.invoke({"resume_text": resume_text})
            
            # Convert to dict for your existing pipeline
            return {
                "extracted_skills": [
                    {"name": s.name, "years": s.years_experience, "context": s.context} 
                    for s in result.skills
                ],
                "inferred_intent": result.intent,
                "detected_velocity": result.learning_velocity_indicator
            }
        except Exception as e:
            # Fallback for production robustness
            print(f"LLM Extraction Failed: {e}")
            return {"extracted_skills": [], "inferred_intent": "OPEN_TO_WORK", "detected_velocity": 1.0}

    def _create_persona(self, user_id: str, data: Dict) -> Dict:
        return {
            "id": str(uuid4()),
            "user_id": user_id,
            "state": "PASSIVE_LISTENING",
            "creation_date": datetime.now().isoformat(),
            "configuration": {
                "autonomy_level": "LOW",
                "privacy_setting": "ZERO_KNOWLEDGE_PROOF"
            }
        }

    def _generate_initial_signal(self, agent_id: str, data: Dict) -> Dict:
        vectors = {}
        for skill in data['extracted_skills']:
            # Innovation Logic: Convert Time to Confidence.
            confidence = min(skill['years'] * 0.15, 0.9) 
            vectors[skill['name']] = confidence

        return {
            "agent_id": agent_id,
            "intent": data['inferred_intent'],
            "verified_vectors": vectors,
            "learning_velocity": data['detected_velocity'],
            "timestamp": datetime.now().isoformat()
        }

    def _backfill_behavior_log(self, user_id: str, data: Dict) -> List[Dict]:
        logs = []
        for skill in data['extracted_skills']:
            logs.append({
                "user_id": user_id,
                "action_type": "LEGACY_IMPORT",
                "details": f"Claimed {skill['years']} years of {skill['name']}",
                "impact_score": 0.5,
                "timestamp": datetime.now().isoformat()
            })
        return logs
