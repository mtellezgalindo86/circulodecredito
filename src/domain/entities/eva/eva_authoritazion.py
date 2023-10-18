from pydantic import BaseModel
from typing import Optional


class Acknowledgement(BaseModel):
    acknowledgeId: Optional[str] = None
    dateTime: Optional[str] = None
    operation: Optional[str] = None
    message: Optional[str] = None
    employmentVerificationRequestId: Optional[str] = None
    subscriptionId: Optional[str] = None
    inquiryId: Optional[str] = None
