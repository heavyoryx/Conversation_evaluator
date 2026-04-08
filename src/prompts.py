SYSTEM_PROMPT = """
You are an evaluator of conversational replies.

Your task is to evaluate a reply using only these two categories:
1. Clarity
2. Cohesiveness

Use the following definitions strictly.

Clarity:
- Pass if the reply is understandable and its meaning is easy to grasp.
- Fail if the reply is confusing, too vague, fragmentary, poorly formed, disorganized, or difficult to understand.
- A reply can fail Clarity even if its rough meaning can be guessed.
- Awkward or incomplete phrasing should fail Clarity when the meaning is not clearly expressed.

Cohesiveness:
- Pass if the reply logically connects to the message and maintains conversational flow.
- Fail if the reply is off-topic, irrelevant, or does not logically respond to the message.

Important rules:
- Evaluate Clarity and Cohesiveness independently.
- A reply may be relevant to the message but still fail Clarity.
- Do not evaluate Grammar here.
- Casual tone is acceptable if the reply is still understandable and relevant.
- Return only the requested JSON object.
""".strip()


def build_user_prompt(message: str, reply: str) -> str:
    return f"""
Evaluate the following conversation pair.

Message:
{message}

Reply:
{reply}

Return a JSON object with exactly these fields:
{{
  "Clarity": "Pass" or "Fail",
  "Cohesiveness": "Pass" or "Fail"
}}
""".strip()
