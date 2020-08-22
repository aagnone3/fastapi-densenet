from fastapi_sentiment import sentiment_analysis


def test_shape_get_sentiment():
    response = sentiment_analysis.get_sentiment("I love tests")
    for key in ['pos', 'neg', 'neu', 'compound']:
        assert key in response
        assert response[key] >= -1 and response[key] <= 1


def test_values_get_sentiment():
    response = sentiment_analysis.get_sentiment("I love tests")
    assert response == {
        'compound': 0.6369,
        'neg': 0.0,
        'neu': 0.192,
        'pos': 0.808
    }
