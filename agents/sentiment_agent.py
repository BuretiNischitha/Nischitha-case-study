from pydantic import BaseModel
from agents.schemas import TicketInput
from agents.base_agent import AIAgent  # Use custom one

class SentimentOutput(BaseModel):
    sentiment: str
    urgency_level: str
    emotional_intensity: str

class SentimentAgent(AIAgent[TicketInput, SentimentOutput]):
    output_model = SentimentOutput
    prompt_template = """
    Analyze the following customer support ticket and respond with a JSON object like:
    {
        "sentiment": "...",
        "urgency_level": "...",
        "emotional_intensity": "..."
    }

    Subject: {subject}
    Message: {message}
    """


