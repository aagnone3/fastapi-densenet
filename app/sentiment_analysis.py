from typing import Dict

from nltk.sentiment.vader import SentimentIntensityAnalyzer

ANALYZER = SentimentIntensityAnalyzer()


def get_sentiment(document: Dict[str, str]) -> Dict[str, float]:
    return ANALYZER.polarity_scores(document)
