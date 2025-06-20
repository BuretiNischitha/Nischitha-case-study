from agents.sentiment_agent import SentimentAgent
from agents.routing_agent import RoutingAgent
from agents.schemas import CombinedTicket
from evaluation.test_cases import test_cases

# Initialize agents
sentiment_agent = SentimentAgent()
routing_agent = RoutingAgent()

# Run each test case
for ticket in test_cases:
    print(f"\nTicket ID: {ticket.ticket_id}")

    sentiment = sentiment_agent.run(ticket)
    print("Sentiment Output:", sentiment)

    combined = CombinedTicket(
        **ticket.model_dump(),
        sentiment=sentiment.sentiment,
        urgency_level=sentiment.urgency_level,
        emotional_intensity=sentiment.emotional_intensity
    )

    routing = routing_agent.run(combined)
    print("Routing Output:", routing)

