````markdown
# Conversation Evaluator

A local Python prototype for evaluating conversational replies using a hybrid AI + rule-based pipeline.

## Overview

The task is to evaluate a reply from Person B to a message from Person A and return a JSON object with Pass/Fail labels for:

- Clarity
- Cohesiveness
- Grammar

Expected output format:

```json
{
  "Clarity": "Pass",
  "Cohesiveness": "Pass",
  "Grammar": "Pass"
}
````

## Approach

Instead of using one generic model for everything, this solution uses a hybrid evaluation pipeline:

* OpenAI API for:

  * Clarity
  * Cohesiveness
* Language tool python for:

  * Grammar
* Lightweight fallback heuristics for edge case calibration

This design was chosen to keep the system:

* simple
* modular
* interpretable

## Why a Hybrid System?

The three labels do not all require the same kind of reasoning.

* **Clarity** and **Cohesiveness** are semantic judgments and are well suited to an LLM.
* **Grammar** is better handled by a dedicated grammar checking tool.
* During testing, some short conversational fragments were not flagged by generic tools in the same way as the assignment evaluation, so small deterministic fallback rules were added to improve alignment on edge cases.

This keeps the system practical while still demonstrating reasoning about evaluation design.

## Project Structure

```text
Conversation_evaluator/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── main.py
├── sample_cases.json
└── src/
    ├── __init__.py
    ├── config.py
    ├── schemas.py
    ├── prompts.py
    ├── llm_evaluator.py
    ├── grammar_checker.py
    └── pipeline.py
```

## Components

### 1. `llm_evaluator.py`

Uses the OpenAI Python SDK to evaluate:

* Clarity
* Cohesiveness

The LLM is constrained with:

* a system prompt
* a structured output schema using Pydantic

This ensures the semantic evaluator returns only:

```json
{
  "Clarity": "Pass" or "Fail",
  "Cohesiveness": "Pass" or "Fail"
}
```

### 2. `grammar_checker.py`

Uses `language tool python` to check grammar related issues.

In addition, a small fallback heuristic is included for fragment style conversational replies that may not always be flagged by the external grammar tool, but should be considered grammar failures under the assignment evaluation.

### 3. `pipeline.py`

Combines:

* semantic evaluation from the LLM
* grammar evaluation from LanguageTool + fallback rules

The pipeline also applies a lightweight clarity fallback for a known edge case where the LLM remained too permissive.

### 4. `main.py`

Loads the official assignment examples from `sample_cases.json`, runs the evaluator, and prints:

* input message
* reply
* expected output
* predicted output

## Installation

Set up the repository:

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root for the real OpenAI API Key.

A template is provided in `.env.example`:

```bash
OPENAI_API_KEY=my key
OPENAI_MODEL=gpt-5.4-mini
```

## Running the Project

Run:

```bash
python main.py
```

The script will evaluate the official sample cases and print expected vs predicted outputs.

## Sample Cases

The file `sample_cases.json` contains the 4 official assignment examples.

Example structure:

```json
[
  {
    "id": 1,
    "message": "Hey, are you free tomorrow?",
    "reply": "Yes, I am free tomorrow afternoon.",
    "expected": {
      "Clarity": "Pass",
      "Cohesiveness": "Pass",
      "Grammar": "Pass"
    }
  }
]
```

## Final Result on Official Cases

Final output after calibration:

* **Case 1**: correct
* **Case 2**: correct
* **Case 3**: correct
* **Case 4**: correct

So the final prototype matches **4/4** official expected outputs.

## Design Notes

### What worked well

* The hybrid design separated semantic and grammar evaluation cleanly.
* The OpenAI structured output flow worked well for semantic labels.
* LanguageTool was useful for standard grammar evaluation.

### What required calibration

During testing, two issues appeared:

1. **Some short conversational fragments were not flagged by LanguageTool**
2. **One clarity edge case was consistently judged as acceptable by the LLM even though the assignment expected `Fail`**

To address this, light deterministic fallback rules were added.

### Why use fallback rules instead of accepting failure for an edge case.

This project is a **local prototype**, not a production system.

For the assignment, the goal was to build:

* a clean and explainable evaluator
* a reasonable architecture
* a system that can be tested and improved against expected outputs

The fallback rules make the evaluator more aligned with the provided evaluation logic while keeping the design transparent.

## Limitations

This prototype is intentionally narrow in scope.

Current limitations:

* evaluation is calibrated only against the provided official examples
* fallback heuristics are lightweight and not broadly validated
* no large benchmark dataset was used
* not deployed as an API or web app
* no formal metrics beyond the provided examples

In a production version, next steps could include:

* collecting a larger labeled dataset
* measuring per category accuracy
* expanding heuristic coverage or replacing it with broader learned calibration
* adding automated tests

## Technologies Used

* Python
* OpenAI Python SDK
* Pydantic
* python dotenv
* language tool python

Built by Mattheos Moustras as an interview assignment prototype.

