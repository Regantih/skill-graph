import os
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Force port 5455 for this check
os.environ["POSTGRES_PORT"] = "5455"

from backend.database import engine

def check_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Database connection successful!")
            
            # Check for Age extension
            try:
                connection.execute(text("LOAD 'age'"))
                print("Apache AGE extension loaded successfully.")
            except Exception as e:
                print(f"Warning: Could not load AGE extension: {e}")
                
    except Exception as e:
        print(f"Database connection failed: {e}")
        exit(1)

if __name__ == "__main__":
    check_connection()
