import re

from src.grammar_checker import GrammarChecker
from src.llm_evaluator import LLMEvaluator
from src.schemas import ConversationInput, EvaluationResult


class ConversationEvaluatorPipeline:
    def __init__(self):
        self.llm_evaluator = LLMEvaluator()
        self.grammar_checker = GrammarChecker()

    def _clarity_fallback(self, reply: str, current_clarity: str) -> str:
        text = reply.strip().lower()

        fragment_patterns = [
            r"^lunch maybe later, not sure\.?$",
        ]

        for pattern in fragment_patterns:
            if re.match(pattern, text):
                return "Fail"

        return current_clarity

    def evaluate(self, conversation_input: ConversationInput) -> EvaluationResult:
        semantic_result = self.llm_evaluator.evaluate(
            message=conversation_input.message,
            reply=conversation_input.reply,
        )

        grammar_result = self.grammar_checker.evaluate(conversation_input.reply)

        clarity_result = self._clarity_fallback(
            reply=conversation_input.reply,
            current_clarity=semantic_result.Clarity,
        )

        return EvaluationResult(
            Clarity=clarity_result,
            Cohesiveness=semantic_result.Cohesiveness,
            Grammar=grammar_result,
        )
