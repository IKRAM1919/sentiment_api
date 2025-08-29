from pydantic import BaseModel

class TextPayload(BaseModel):
    """
    Represents the input payload for sentiment analysis.
    """
    text: str

class PredictionResponse(BaseModel):
    """
    Represents the output response from the sentiment analysis API.
    """
    sentiment: str
    score: float