# tools/sentiment_tool.py

from google.adk.tools import Tool
from textblob import TextBlob


def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment of a given text and return polarity score and classification.

    Args:
        text (str): Input news or summary text.

    Returns:
        dict: Sentiment score and label.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "polarity_score": round(polarity, 3),
        "sentiment": label
    }


analyze_sentiment = Tool.from_function(analyze_sentiment)
