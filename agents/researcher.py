from crewai import Agent


class ResearcherAgent:
    def __init__(self):
        self.agent = Agent(
            name="Market Researcher",
            role="Scans financial news, trends, and reports",
            model="gpt-4",
            description="Fetches latest market trends and provides insights."
        )

    def fetch_trends(self, stock_symbol):
        return self.agent.run(f"Fetch the latest market trends for {stock_symbol}")
