from pydantic import BaseModel
# Input to SentimentAgent
class TicketInput(BaseModel):
    ticket_id: str
    customer_tier: str
    subject: str
    message: str
    previous_tickets: int
    monthly_revenue: float
    account_age_days: int

# Output of SentimentAgent
class SentimentOutput(BaseModel):
    sentiment: str
    urgency_level: str
    emotional_intensity: str

# Input to RoutingAgent ( combined(ticket + sentiment))
class CombinedTicket(BaseModel):
    ticket_id: str
    customer_tier: str
    subject: str
    message: str
    previous_tickets: int
    monthly_revenue: float
    account_age_days: int
    sentiment: str
    urgency_level: str
    emotional_intensity: str

# Output of RoutingAgent
class RoutingOutput(BaseModel):
    priority: str
    recommended_team: str
    escalation_needed: bool
