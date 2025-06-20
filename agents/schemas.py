from pydantic import BaseModel

class TicketInput(BaseModel):
    ticket_id: str
    customer_tier: str  # free / premium / enterprise
    subject: str
    message: str
    previous_tickets: int
    monthly_revenue: float
    account_age_days: int

