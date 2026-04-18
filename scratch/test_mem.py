import sys
import os
import pandas as pd
import joblib
from analytics_system.utils import PLAYER_MODEL_PATH

def test_load():
    print(f"Attempting to load: {PLAYER_MODEL_PATH}")
    try:
        model = joblib.load(PLAYER_MODEL_PATH)
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_load()
