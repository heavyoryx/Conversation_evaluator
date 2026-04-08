import json
from pathlib import Path

from src.pipeline import ConversationEvaluatorPipeline
from src.schemas import ConversationInput


def main():
    sample_file = Path("sample_cases.json")

    if not sample_file.exists():
        raise FileNotFoundError("sample_cases.json was not found in the project root.")

    with sample_file.open("r", encoding="utf-8") as f:
        cases = json.load(f)

    pipeline = ConversationEvaluatorPipeline()

    for case in cases:
        conversation = ConversationInput(
            message=case["message"],
            reply=case["reply"],
        )

        result = pipeline.evaluate(conversation)

        print(f"\nCase {case['id']}")
        print(f"Message: {case['message']}")
        print(f"Reply: {case['reply']}")
        print("Expected:")
        print(json.dumps(case["expected"], indent=2))
        print("Predicted:")
        print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
