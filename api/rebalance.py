from fastapi import APIRouter
from pipelines.rebalancer import PortfolioRebalancer

router = APIRouter()


@router.post("/rebalance")
def rebalance_portfolio(user_portfolio: dict):
    target_allocation = {"stocks": 0.6, "bonds": 0.3, "cash": 0.1}
    rebalancer = PortfolioRebalancer(target_allocation)
    adjustments = rebalancer.rebalance(user_portfolio)
    return {"adjustments": adjustments}
