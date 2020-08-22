def test_basic(api_client):
    response = api_client.get('/')
    assert response.status_code == 200
    assert response.json() == {
        'message': 'Hello World'
    }

def test_get_health(api_client):
    response = api_client.get('/health')
    assert response.status_code == 200
    assert response.json() == {
        'message': "Still kicking"
    }

def test_sentiment(api_client):
    response = api_client.post('/sentiment', json={
        'text': 'I love tests'
    })
    assert response.status_code == 200
    assert response.json() == {
        'compound': '0.6369',
        'neg': '0.0',
        'neu': '0.192',
        'pos': '0.808'
    }
