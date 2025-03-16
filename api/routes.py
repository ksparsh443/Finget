from fastapi import FastAPI
from agents.planner import PlannerAgent
from api.alerts import router as alerts_router
app = FastAPI()
app.include_router(alerts_router)


@app.get("/plan/{user_profile}")
def get_plan(user_profile: str):
    planner = PlannerAgent()
    return {"plan": planner.plan_investment(user_profile)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
