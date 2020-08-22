from pydantic import BaseModel

class SentimentDocument(BaseModel):
    text: str

class SentimentScoring(BaseModel):
    pos: str
    neg: str
    neu: str
    compound: str
