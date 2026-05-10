from pydantic import BaseModel
from typing import List


class SkillRequest(BaseModel):

    user_skills: List[str]
    target_role: str


class SkillResponse(BaseModel):

    matched: List[str]
    missing: List[str]
    extra: List[str]
    readiness_score: float