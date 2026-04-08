from src.grammar_checker import GrammarChecker
from src.llm_evaluator import LLMEvaluator
from src.schemas import ConversationInput, EvaluationResult


class ConversationEvaluatorPipeline:
    def __init__(self):
        self.llm_evaluator = LLMEvaluator()
        self.grammar_checker = GrammarChecker()

    def evaluate(self, conversation_input: ConversationInput) -> EvaluationResult:
        semantic_result = self.llm_evaluator.evaluate(
            message=conversation_input.message,
            reply=conversation_input.reply,
        )

        grammar_result = self.grammar_checker.evaluate(conversation_input.reply)

        return EvaluationResult(
            Clarity=semantic_result.Clarity,
            Cohesiveness=semantic_result.Cohesiveness,
            Grammar=grammar_result,
        )
