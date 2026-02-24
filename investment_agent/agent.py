# agent.py

from google.adk.agents import Agent
from google.adk.tools import google_search
from sub_agents.news_agent import news_agent

# Root Orchestrator Agent
investment_orchestrator = Agent(
    name="InvestmentOrchestrator",
    model="gemini-1.5-pro",  # Stable model (no -exp)
    description="Orchestrates financial research and generates investment insights.",
    instruction="""
You are the root orchestrator agent.

When a user asks about a company:
1. Delegate news-related research to the NewsResearchAgent.
2. Collect the structured response.
3. Present a clean summary to the user.

Ensure responses are structured and professional.
""",
    tools=[google_search],
    sub_agents=[news_agent],
)

root_agent = investment_orchestrator