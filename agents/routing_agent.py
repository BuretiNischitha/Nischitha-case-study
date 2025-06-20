from pydantic_ai.agent import AIAgent
from pydantic import BaseModel
from agents.schemas import TicketInput
from agents.sentiment_agent import SentimentOutput

class RoutingOutput(BaseModel):
    priority: str               # low, medium, high
    recommended_team: str       # support, engineering, account manager
    escalation_needed: bool

class RoutingAgent(AIAgent[tuple[TicketInput, SentimentOutput], RoutingOutput]):
    prompt_template = """
    Given the customer details and sentiment analysis, determine:
    - Ticket priority
    - Which team should handle it
    - Whether escalation is needed

    Customer Tier: {0.customer_tier}
    Previous Tickets: {0.previous_tickets}
    Revenue: {0.monthly_revenue}
    Account Age: {0.account_age_days}

    Sentiment: {1.sentiment}
    Urgency: {1.urgency_level}
    Intensity: {1.emotional_intensity}
    """

