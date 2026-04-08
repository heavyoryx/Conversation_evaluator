from typing import Literal

from pydantic import BaseModel, Field


PassFail = Literal["Pass", "Fail"]


class ConversationInput(BaseModel):
    message: str = Field(..., min_length=1, description="Message from Person A.")
    reply: str = Field(..., min_length=1, description="Reply from Person B.")


class EvaluationResult(BaseModel):
    Clarity: PassFail = Field(..., description="Pass or Fail for clarity.")
    Cohesiveness: PassFail = Field(..., description="Pass or Fail for cohesiveness.")
    Grammar: PassFail = Field(..., description="Pass or Fail for grammar.")


class SemanticEvaluationResult(BaseModel):
    Clarity: PassFail = Field(..., description="Pass or Fail for clarity.")
    Cohesiveness: PassFail = Field(..., description="Pass or Fail for cohesiveness.")
