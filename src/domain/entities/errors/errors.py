from pydantic import BaseModel
from typing import List


class ErrorEntry(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    errors: List[ErrorEntry]
