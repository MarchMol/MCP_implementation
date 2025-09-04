import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder containing resources.py
CSV_PATH = os.path.join(BASE_DIR, "data", "emoji_usage_dataset.csv")

df = pd.read_csv(CSV_PATH)

# ---- Dataset description ---- #
def get_contexts():
    """
    Returns list of possible contexts or feelings associated to an emoji
    """
    return df["Context"].unique().tolist()
    
def get_platforms():
    """
    Returns list of possible sentiments in an emoji
    """
    return df["Platform"].unique().tolist()

def is_valid_emoji(emoji: str = ""):
    """
    Returns a boolean value if a given emoji exists in the dataest
    """
    return df["Emoij"].isin([emoji]).any()
