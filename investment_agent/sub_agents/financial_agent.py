from google.adk.agents import Agent
from tools.stock_tool import fetch_stock_data

financial_agent = Agent(
    name="FinancialAnalysisAgent",
    model="gemini-1.5-pro",
    description="Fetches stock data and computes financial metrics.",
    instruction="""
You are a financial analysis agent.

When given a company stock symbol:
1. Use fetch_stock_data tool.
2. Analyze:
   - Current price
   - 30-day return
   - Volatility
3. Provide structured financial insights.
""",
    tools=[fetch_stock_data],
)