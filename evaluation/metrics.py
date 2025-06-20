from evaluation.test_cases import test_cases
from agents.sentiment_agent import SentimentAgent
from agents.routing_agent import RoutingAgent
from agents.schemas import CombinedTicket
#Summarizing everything
sentiment_agent = SentimentAgent()
routing_agent = RoutingAgent()
summary = []
for ticket in test_cases:
    sentiment = sentiment_agent.run(ticket)
    combined = CombinedTicket(
        **ticket.model_dump(),
        sentiment=sentiment.sentiment,
        urgency_level=sentiment.urgency_level,
        emotional_intensity=sentiment.emotional_intensity
    )
    routing = routing_agent.run(combined)
    summary.append({
        "ticket_id": ticket.ticket_id,
        "sentiment": sentiment.dict(),
        "routing": routing.dict()
    })
print("\n Evaluation Summary:")
for result in summary:
    print(f"Ticket: {result['ticket_id']}")
    print("  Sentiment:", result["sentiment"])
    print("  Routing  :", result["routing"])
    print("-" * 40)

