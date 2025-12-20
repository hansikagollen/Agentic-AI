from tools.schemes_db import load_schemes
from tools.eligibility import check_eligibility

def execute(memory):
    schemes = load_schemes()
    eligible = []

    for scheme in schemes:
        if check_eligibility(memory, scheme):
            eligible.append(scheme)

    return eligible
