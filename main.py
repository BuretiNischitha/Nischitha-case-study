from agents.sentiment_agent import SentimentAgent
from agents.routing_agent import RoutingAgent
from agents.schemas import TicketInput, CombinedTicket

# Define a reusable function to process a ticket
def process_ticket(ticket: TicketInput):
    sentiment_agent = SentimentAgent()
    sentiment_result = sentiment_agent.run(ticket)
    print("\n Sentiment Output for", ticket.ticket_id, ":", sentiment_result)

    combined = CombinedTicket(
        **ticket.model_dump(),
        sentiment=sentiment_result.sentiment,
        urgency_level=sentiment_result.urgency_level,
        emotional_intensity=sentiment_result.emotional_intensity
    )

    routing_agent = RoutingAgent()
    routing_result = routing_agent.run(combined)
    print(" Routing Output for", ticket.ticket_id, ":", routing_result)

# All 5 official test cases
test_cases = [
    TicketInput(
        ticket_id="SUP-001",
        customer_tier="free",
        subject="This product is completely broken!!!",
        message="Nothing works! I can't even log in. This is the worst software I've ever used.",
        previous_tickets=0,
        monthly_revenue=0,
        account_age_days=2
    ),
    TicketInput(
        ticket_id="SUP-002",
        customer_tier="enterprise",
        subject="Minor UI issue with dashboard",
        message="Hi team, just noticed the dashboard numbers are slightly misaligned on mobile view.",
        previous_tickets=15,
        monthly_revenue=25000,
        account_age_days=730
    ),
    TicketInput(
        ticket_id="SUP-003",
        customer_tier="premium",
        subject="Feature Request: Bulk export",
        message="We need bulk export functionality for our quarterly reports. Currently exporting one by one is too slow.",
        previous_tickets=5,
        monthly_revenue=5000,
        account_age_days=400
    ),
    TicketInput(
        ticket_id="SUP-004",
        customer_tier="premium",
        subject="API rate limits unclear",
        message="Getting rate limited but documentation says we should have 1000 requests/hour. We're confused.",
        previous_tickets=8,
        monthly_revenue=3000,
        account_age_days=180
    ),
    TicketInput(
        ticket_id="SUP-005",
        customer_tier="enterprise",
        subject="Urgent: Security vulnerability?",
        message="Our security team flagged that your API responses include internal server paths in error messages.",
        previous_tickets=20,
        monthly_revenue=50000,
        account_age_days=900
    )
]
# Run all test cases
for ticket in test_cases:
    process_ticket(ticket)

