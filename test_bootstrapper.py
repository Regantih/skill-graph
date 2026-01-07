import os
import sys

# Ensure we can import from backend
sys.path.append(os.getcwd())

from backend.core.conversion import AgentBootstrapper

def test_ignition():
    print("🚀 IGNITION SEQUENCE START: Testing Agent Bootstrapper...")
    
    # 1. Sample Resume Text
    resume_text = """
    JANE DOE
    Senior Software Engineer
    
    EXPERIENCE
    Senior Python Developer | TechCorp | 2020 - Present
    - Architected microservices using FastAPI and PostgreSQL.
    - Led a team of 4 developers.
    
    Data Scientist | DataInc | 2018 - 2020
    - Built predictive models using Scikit-Learn and Pandas.
    - Deployed models to AWS Lambda.
    
    SKILLS
    Python, FastAPI, AWS, Docker, PostgreSQL, Machine Learning
    """
    
    # 2. Initialize
    # Note: Requires OPENAI_API_KEY env var for real LLM, otherwise Mock.
    bootstrapper = AgentBootstrapper()
    
    user_id = "user_test_001"
    
    # 3. Execute
    print(f"Analyzing resume for User: {user_id}...")
    result = bootstrapper.bootstrap_agent(user_id, resume_text)
    
    # 4. Inspect Output
    persona = result['persona']
    signal = result['signal']
    
    print("\n✅ AGENT BORN SUCCESSFULLY!")
    print(f"ID: {persona['id']}")
    print(f"State: {persona['state']}")
    print("-" * 30)
    print("📡 PUBLIC SIGNAL BROADCAST:")
    print(f"Intent: {signal['intent']}")
    print(f"Velocity: {signal['learning_velocity']}")
    print("Verified Vectors (Confidence Scores):")
    for skill, score in signal['verified_vectors'].items():
        print(f"  - {skill}: {score:.2f}")
        
if __name__ == "__main__":
    test_ignition()
