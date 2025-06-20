from agents.base_agent import AIAgent
from agents.schemas import TicketInput, SentimentOutput
# Agent to extract sentiment, urgency, and intensity
class SentimentAgent(AIAgent[TicketInput, SentimentOutput]):
    output_model = SentimentOutput
    prompt_template = """
You are a customer support sentiment analyzer.

Your job is to extract exactly 3 things:
1. Sentiment (positive, neutral, negative)
2. Urgency level (low, medium, high)
3. Emotional intensity (calm, moderate, intense)

ONLY respond with JSON exactly in this format:
{
  "sentiment": "negative",
  "urgency_level": "high",
  "emotional_intensity": "intense"
}

No explanations. No comments. No markdown. Just JSON.

Ticket:
Subject: {subject}
Message: {message}
"""
