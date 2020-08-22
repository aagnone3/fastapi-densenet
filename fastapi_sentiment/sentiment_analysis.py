from typing import Dict

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_sentiment(document: Dict[str, str]) -> Dict[str, float]:
    return SentimentIntensityAnalyzer().polarity_scores(document)
