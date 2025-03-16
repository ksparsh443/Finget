from crewai import Agent


class AnalystAgent:
    def __init__(self):
        self.agent = Agent(
            name="Data Analyst",
            role="Analyzes financial metrics and user portfolios",
            model="gpt-4",
            description="Performs risk analysis and trend prediction."
        )

    def analyze_portfolio(self, portfolio):
        return self.agent.run(f"Analyze the following portfolio: {portfolio}")
