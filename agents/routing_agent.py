from pydantic import BaseModel
from agents.schemas import TicketInput
from agents.sentiment_agent import SentimentOutput
from agents.base_agent import AIAgent

class RoutingOutput(BaseModel):
    priority: str
    recommended_team: str
    escalation_needed: bool

class RoutingAgent(AIAgent[tuple[TicketInput, SentimentOutput], RoutingOutput]):
    output_model = RoutingOutput

    def run(self, input_data: tuple[TicketInput, SentimentOutput]) -> RoutingOutput:
        ticket, sentiment = input_data
        prompt = self.prompt_template.format(ticket, sentiment)
        return super().run(input_data=type("Combined", (BaseModel,), {
            **ticket.dict(),
            **sentiment.dict()
        })())

    prompt_template = """
    Based on the ticket and sentiment analysis, respond with a JSON object like:
    {
        "priority": "...",
        "recommended_team": "...",
        "escalation_needed": ...
    }

    Ticket Info:
    Customer Tier: {customer_tier}
    Previous Tickets: {previous_tickets}
    Revenue: {monthly_revenue}
    Account Age: {account_age_days}

    Sentiment: {sentiment}
    Urgency: {urgency_level}
    Intensity: {emotional_intensity}
    """
