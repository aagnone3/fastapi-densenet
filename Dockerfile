FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Args
ARG WORKING_DIRECTORY

# System-related
WORKDIR ${WORKING_DIRECTORY}
COPY . .

# Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# NLTK downloads
RUN python3 -c "import nltk; nltk.download('vader_lexicon')"