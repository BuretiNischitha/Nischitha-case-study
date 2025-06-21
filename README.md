# Nischitha-case-study
# Multi-Agent AI System for Intelligent Decision Making
## Problem Statement
In many domains—such as customer service, operations, HR, and EdTech—organizations struggle to process large volumes of unstructured data (like tickets, messages, and reviews). Relying on one large model to do everything leads to:
- Poor output consistency
- Hard-to-debug logic
- Limited reusability
- Low flexibility across tasks

---
## Solution Overview
This project introduces a **modular, multi-agent AI system** using:
- Pydantic for input/output validation
- Prompt-engineered LLMs via OpenRouter
- Clean, chainable agent logic
- Structured, readable, and testable architecture
Each agent performs one specific role in a chain of intelligent reasoning. The outputs are fully validated and can be used in real-world APIs, CRMs, dashboards, or auto-responders.
❗Note: This project was intended to use the pydantic-ai library. However, due to broken versions and missing compatibility in pydantic-ai during development (such as missing AIAgent support and unavailable slim dependencies), a custom agent base class was built from scratch using Pydantic + OpenRouter. The functionality and architecture remain true to the spirit of the case study.
---

## Where This Can Be Applied

| Industry        | Use Case                                          |
|-----------------|---------------------------------------------------|
| Customer Support | Analyze and route support tickets automatically |
| Operations        | Classify and prioritize incoming issues        |
|  Chatbots          | Understand user tone + escalate when needed   |
| HR / Hiring       | Screen applicants based on form + message tone |
| EdTech            | Auto-respond to student queries with routing   |

---

## System Architecture
Raw Input ➡️ SentimentAgent ➡️ CombinedTicket ➡️ RoutingAgent ➡️ Final Decision
## Folder Structure
your-name-case-study/
├── main.py # Entry point: runs all agents
├── agents/
│ ├── base_agent.py # Reusable AIAgent class
│ ├── sentiment_agent.py # Agent 1: Extracts sentiment & urgency
│ ├── routing_agent.py # Agent 2: Makes final decision
│ └── schemas.py # Input/output data models
├── evaluation/
│ ├── test_cases.py # Sample ticket inputs
│ ├── run_tests.py # Run all test cases
│ └── metrics.py # (Optional) Summary reports
├── docs/
│ └── architecture.md # Full architecture + prompt design
├── ai_chat_history.txt # Full chat with AI (for transparency)
└── README.md # This file
