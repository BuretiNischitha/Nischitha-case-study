from agents.base_agent import AIAgent
from agents.schemas import CombinedTicket, RoutingOutput
# Agent to route ticket based on business,emotional factors
class RoutingAgent(AIAgent[CombinedTicket, RoutingOutput]):
    output_model = RoutingOutput
    prompt_template = """
Given the ticket and sentiment, respond with JSON:
{
  "priority": "high",
  "recommended_team": "engineering",
  "escalation_needed": true
}

Customer Tier: {customer_tier}
Previous Tickets: {previous_tickets}
Monthly Revenue: {monthly_revenue}
Account Age: {account_age_days}
Sentiment: {sentiment}
Urgency: {urgency_level}
Intensity: {emotional_intensity}
"""
