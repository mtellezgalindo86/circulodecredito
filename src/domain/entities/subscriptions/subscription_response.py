from pydantic import BaseModel
from typing import Optional


class Subscription(BaseModel):
    eventType: Optional[str] = None
    webHookUrl: Optional[str] = None
    enrollmentId: Optional[str] = None
    subscriptionId: Optional[str] = None
    dateTime: Optional[str] = None


class SubscriptionResponse(BaseModel):
    acknowledgeId: Optional[str] = None
    dateTime: Optional[str] = None
    operation: Optional[str] = None
    message: Optional[str] = None
    subscription: Optional[Subscription]
