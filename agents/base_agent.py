import os
import json
import requests
from typing import Type, Generic, TypeVar
from pydantic import BaseModel

# type variables for input/output
I = TypeVar("I", bound=BaseModel)
O = TypeVar("O", bound=BaseModel)

# base agent class for all agents
class AIAgent(Generic[I, O]):
    output_model: Type[O]
    prompt_template: str

    def __init__(self):
        if not hasattr(self, "prompt_template"):
            raise NotImplementedError("You must define a prompt_template.")
        if not hasattr(self, "output_model"):
            raise NotImplementedError("You must define an output_model.")

    def run(self, input_data: I) -> O:
        prompt = self.prompt_template.format(**input_data.model_dump())

        headers = {
            "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
            "HTTP-Referer": "https://openrouter.ai",
            "X-Title": "pydantic-ai-case-study"
        }

        body = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that responds only with valid JSON."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body
        )

        reply = response.json()["choices"][0]["message"]["content"]

        try:
            json_start = reply.find("{")
            json_str = reply[json_start:]
            json_data = json.loads(json_str)
        except Exception as e:
            print("Failed to parse JSON. Full reply:")
            print(reply)
            raise e

        return self.output_model(**json_data)
