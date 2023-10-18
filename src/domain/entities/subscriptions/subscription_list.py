from typing import List, Optional
from pydantic import BaseModel


class Links(BaseModel):
    self: Optional[str] = None
    first: Optional[str] = None
    previous: Optional[str] = None
    next: Optional[str] = None
    last: Optional[str] = None


class Metadata(BaseModel):
    page: Optional[int] = None
    perPage: Optional[int] = None
    pageCount: Optional[int] = None
    totalCount: Optional[int] = None
    links: Optional[Links] = None


class SubscriptionItem(BaseModel):
    eventType: Optional[str] = None
    webHookUrl: Optional[str] = None
    enrollmentId: Optional[str] = None
    subscriptionId: Optional[str] = None
    dateTime: Optional[str] = None


class SubscriptionResponseList(BaseModel):
    _metadata: Optional[Metadata] = None
    subscriptions: Optional[List[SubscriptionItem]] = None
