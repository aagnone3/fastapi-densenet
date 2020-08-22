FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# System-related
WORKDIR /app
COPY . .

# Install package
RUN pip3 install --upgrade pip && \
    python3 setup.py install

# NLTK downloads
RUN python3 -c "import nltk; nltk.download('vader_lexicon')"

# Networking
EXPOSE 80

ENV APP_MODULE='fastapi_sentiment.main:app'