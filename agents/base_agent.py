# agents/base_agent.py

import os
import openai
from pydantic import BaseModel
from typing import Type, Generic, TypeVar

# Setup OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

I = TypeVar("I", bound=BaseModel)  # Input model
O = TypeVar("O", bound=BaseModel)  # Output model

class AIAgent(Generic[I, O]):
    input_model: Type[I]
    output_model: Type[O]
    prompt_template: str

    def __init__(self):
        if not hasattr(self, "prompt_template"):
            raise NotImplementedError("You must define a prompt_template string.")

    def run(self, input_data: I) -> O:
        prompt = self.prompt_template.format(**input_data.dict())
        print("🧠 Prompt sent to OpenAI:\n", prompt)  # Optional debug print

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that returns only structured JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        text = response['choices'][0]['message']['content']
        try:
            json_data = eval(text) if text.startswith("{") else eval("{" + text.split("{", 1)[1])
        except Exception as e:
            print("⚠️ Error parsing response:", e)
            print("Raw response:\n", text)
            raise e

        return self.output_model(**json_data)

