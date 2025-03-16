import numpy as np


class PortfolioRebalancer:
    def __init__(self, target_allocation):
        """
        target_allocation: {'stocks': 0.6, 'bonds': 0.3, 'cash': 0.1}
        """
        self.target_allocation = target_allocation

    def rebalance(self, portfolio):
        """Rebalances a portfolio based on target allocation"""
        total_value = sum(portfolio.values())
        current_allocation = {k: v / total_value for k, v in portfolio.items()}

        adjustments = {}
        for asset, target_ratio in self.target_allocation.items():
            current_ratio = current_allocation.get(asset, 0)
            difference = target_ratio - current_ratio
            adjustments[asset] = round(difference * total_value, 2)

        return adjustments


rebalancer = PortfolioRebalancer({"stocks": 0.6, "bonds": 0.3, "cash": 0.1})

portfolio = {"stocks": 7000, "bonds": 2000, "cash": 1000}
print(rebalancer.rebalance(portfolio))  # Suggested changes
