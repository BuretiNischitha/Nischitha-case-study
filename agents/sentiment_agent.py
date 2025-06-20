from pydantic_ai.agent import AIAgent
from pydantic import BaseModel
from agents.schemas import TicketInput

class SentimentOutput(BaseModel):
    sentiment: str               # positive, neutral, negative
    urgency_level: str           # low, medium, high
    emotional_intensity: str     # calm, moderate, intense

class SentimentAgent(AIAgent[TicketInput, SentimentOutput]):
    prompt_template = """
    Analyze the following customer support ticket and respond with:
    1. Sentiment (positive, neutral, negative)
    2. Urgency level (low, medium, high)
    3. Emotional intensity (calm, moderate, intense)

    Subject: {subject}
    Message: {message}
    """

