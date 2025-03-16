from crewai import Agent


class PlannerAgent:
    def __init__(self):
        self.agent = Agent(
            name="Investment Planner",
            role="Identifies user goals and crafts investment strategies",
            model="gpt-4",
            description="Creates personalized financial strategies based on market conditions."
        )

    def plan_investment(self, user_profile):
        return self.agent.run(f"Create an investment plan for {user_profile}")
