import csv
import os
from typing import Optional, Dict

CSV_FILE = "applications.csv"


# -----------------------------
# Scheme Decision Logic
# -----------------------------
def decide_scheme(state: Dict) -> Optional[str]:
    """
    Decide eligible government scheme based on user details.
    """

    age = state.get("age")
    income = state.get("income")

    if age is None or income is None:
        return None

    if age >= 60 and income <= 200000:
        return "Old Age Pension Scheme"

    if age >= 18 and income <= 300000:
        return "PM Kisan Scheme"

    return None


# -----------------------------
# Persist Application to CSV
# -----------------------------
def save_application(state: Dict, scheme: str):
    """
    Save eligible application to CSV as proof of action.
    """

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Age", "Income", "Scheme"])

        writer.writerow([
            state.get("name", "Unknown"),
            state.get("age"),
            state.get("income"),
            scheme
        ])
