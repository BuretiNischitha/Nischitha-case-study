from agents.schemas import TicketInput
from agents.sentiment_agent import SentimentAgent
from agents.routing_agent import RoutingAgent

# 1. Sample ticket input
sample_ticket = TicketInput(
    ticket_id="SUP-001",
    customer_tier="enterprise",
    subject="URGENT: Security vulnerability?",
    message="Our security team flagged that your API exposes internal server paths. Please fix this immediately.",
    previous_tickets=15,
    monthly_revenue=50000,
    account_age_days=800
)

# 2. Run Sentiment Agent
sentiment_agent = SentimentAgent()
sentiment_output = sentiment_agent.run(sample_ticket)

# 3. Run Routing Agent
routing_agent = RoutingAgent()
routing_output = routing_agent.run((sample_ticket, sentiment_output))

# 4. Print both results
print("🔍 Sentiment Analysis Result:\n", sentiment_output)
print("\n📬 Routing Decision:\n", routing_output)

