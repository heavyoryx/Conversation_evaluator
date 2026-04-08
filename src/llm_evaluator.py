from openai import OpenAI

from src.config import OPENAI_MODEL, get_openai_api_key
from src.prompts import SYSTEM_PROMPT, build_user_prompt
from src.schemas import SemanticEvaluationResult


class LLMEvaluator:
    def __init__(self):
        self.client = OpenAI(api_key=get_openai_api_key())

    def evaluate(self, message: str, reply: str) -> SemanticEvaluationResult:
        user_prompt = build_user_prompt(message=message, reply=reply)

        response = self.client.responses.parse(
            model=OPENAI_MODEL,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            text_format=SemanticEvaluationResult,
        )

        return response.output_parsed
