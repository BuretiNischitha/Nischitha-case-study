# System Architecture - Multi-Agent AI Framework
-----
## ** Overview:**
This project demonstrates a modular multi-agent AI system built using:
- **Pydantic** for data validation and structure
- **LLMs (via OpenRouter)** for reasoning
- **Prompt engineering** for behavior control
- **Reusable agent classes** to chain intelligent steps
----
## **Why Use Multiple Agents?**
Traditional single-model systems are:
- Hard to debug
- Difficult to scale
- Prone to inconsistent logic
By splitting logic into **focused agents**, each with a clear responsibility, we gain:
-  Simplicity
- Reusability
- Clean input/output guarantees
- Easier testing and iteration
-----
## **Agents in the System:**

### 🟢 Agent 1: Sentiment or Analysis Agent
- **Inputs**: Raw text or data
- **Outputs**: LLM-derived insight (e.g., sentiment, risk score, classification)
- **Use Cases**: Customer service, HR screening, product review analysis

-----

### 🟡 Agent 2: Decision or Routing Agent
- **Inputs**: Combined original data + Agent 1 output
- **Outputs**: Priority, team assignment, flag, or recommendation
- **Use Cases**: Ticket triage, workflow automation, lead scoring
---

## System Components

| Component         | Purpose                                                 |
|------------------|---------------------------------------------------------|
| `schemas.py`     | Structured input/output using `pydantic.BaseModel`     |
| `base_agent.py`  | Generic class for defining agents using prompts        |
| `sentiment_agent.py` | Specialized logic for understanding user emotion    |
| `routing_agent.py`   | Uses structured input to make business decisions    |
| `main.py`        | Entry point to run agents on test data                 |
| `evaluation/`    | Scripts and test cases to validate behavior            |
| `docs/`          | Architecture and reasoning                             |

---

## ⚙️ Prompt Engineering Highlights

Each agent uses a carefully crafted `prompt_template`, filled in dynamically using Python string formatting. Typical structure:
```text
You are an AI that performs task X.
Only return valid JSON in this format:
{
  "key": "value"
}
Input:
{real_input}

