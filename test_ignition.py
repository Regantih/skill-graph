import os
import sys

# Ensure we can import from backend
sys.path.append(os.getcwd())

from backend.core.conversion import AgentBootstrapper

# SAMPLE RESUME: A mix of specific tech and "fuzzy" intent
SAMPLE_RESUME = """
ALEX MERCER
Senior Backend Engineer
Summary:
Obsessed with autonomous systems. 
Over the last 6 months, I've transitioned from Java to Rust, building high-frequency trading bots.
I learned Rust in 3 weeks to meet a deadline.
Tech Stack: Python (8 years), Rust (1 year), Kubernetes, Kafka.
Goal: Looking for a high-autonomy role in a generic AI startup.
"""

def run_test():
    print("🚀 IGNITION SEQUENCE STARTED...")
    
    # 1. Initialize the Bootstrapper (Make sure OPENAI_API_KEY is in env)
    bootstrapper = AgentBootstrapper()
    
    # 2. Run the Conversion Engine
    user_id = "user_test_001"
    result = bootstrapper.bootstrap_agent(user_id, SAMPLE_RESUME)
    
    # 3. Inspect the "Digital Twin"
    persona = result["persona"]
    signal = result["signal"]
    
    print(f"\n✅ AGENT INSTANTIATED: {persona['id']}")
    print(f"   State: {persona['state']}")
    print(f"   Privacy: {persona['configuration']['privacy_setting']}")
    
    print(f"\n📡 BROADCAST SIGNAL GENERATED:")
    print(f"   Intent: {signal['intent']}")
    print(f"   Velocity: {signal['learning_velocity']} (Did it catch the 'learned Rust in 3 weeks'?)")
    print("   Verified Vectors:")
    for skill, score in signal['verified_vectors'].items():
        print(f"     - {skill}: {score:.2f} Confidence")

if __name__ == "__main__":
    # If running directly, assumes you might use dotenv to load keys
    # from dotenv import load_dotenv; load_dotenv()
    run_test()
