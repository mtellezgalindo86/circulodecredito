from pydantic import BaseModel
from typing import Optional


class SubscriptionDataDetail(BaseModel):
    eventType: Optional[str] = None
    webHookUrl: Optional[str] = None
    enrollmentId: Optional[str] = None
    subscriptionId: Optional[str] = None
    dateTime: Optional[str] = None
