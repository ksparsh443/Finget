import numpy as np


class RiskAssessment:
    def calculate_risk(self, portfolio):
        return np.random.uniform(0, 1)  # Dummy risk score


risk = RiskAssessment()
print(risk.calculate_risk({"stocks": ["AAPL", "TSLA"], "cash": 10000}))
