import math
from datetime import datetime, timedelta
from typing import List
from backend.core.schemas import BehaviorLog

class TrustAlgorithm:
    """
    The Math Engine: Converts 'Noise' (Raw Actions) into 'Signal' (Confidence).
    """

    @staticmethod
    def calculate_confidence(logs: List[BehaviorLog]) -> float:
        if not logs:
            return 0.0

        # 1. Volume Score (Diminishing Returns)
        # We use a Tanh function so 1000 commits aren't 10x better than 100.
        # It caps at 1.0.
        raw_volume = sum(log.impact_score for log in logs)
        k = 0.1  # Sensitivity factor. Lower = harder to reach 1.0
        volume_score = math.tanh(k * raw_volume)

        # 2. Recency Decay (The "Rot" Factor)
        # Skills decay if not used. We weight recent logs higher.
        # Logic: Find the most recent log date.
        last_active = max(log.timestamp for log in logs)
        days_diff = (datetime.now() - last_active).days
        
        # Half-life: Signal strength halves every 180 days of inactivity
        decay_half_life = 180 
        recency_multiplier = math.exp(-0.693 * days_diff / decay_half_life)

        # Final Score: Volume * Decay
        # Example: Expert (0.9) who stopped coding 1 year ago (x0.25) = 0.22 Signal
        return round(volume_score * recency_multiplier, 4)

    @staticmethod
    def calculate_velocity(logs: List[BehaviorLog]) -> float:
        """
        Calculates 'Learning Velocity' (Acceleration).
        A high score means the user is acquiring NEW skills rapidly.
        """
        # (Simplified logic for MVP)
        # Ratio of unique skills acquired over the last 30 days vs previous 30
        return 1.2  # Placeholder for complex velocity math
