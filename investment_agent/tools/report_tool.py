from google.adk.tools import Tool


def generate_markdown_report(data: dict) -> str:
    """
    Generate structured markdown investment report.

    Args:
        data (dict): Contains company name, sentiment, and financial metrics.

    Returns:
        str: Markdown formatted report.
    """

    report = f"""
# Investment Brief: {data.get("company", "N/A")}

## Financial Metrics
- Current Price: ₹{data.get("current_price", "N/A")}
- 30-Day Return: {data.get("30_day_return_percent", "N/A")}%
- Volatility: {data.get("volatility", "N/A")}

## News Sentiment
- Sentiment: {data.get("sentiment", "N/A")}
- Polarity Score: {data.get("polarity_score", "N/A")}

## Conclusion
This brief combines short-term price momentum and recent news sentiment
to provide a quick investment snapshot.
"""

    return report


generate_markdown_report = Tool.from_function(generate_markdown_report)