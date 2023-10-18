from pydantic import BaseModel
import uuid
from src.infrastructure.config.contants import EVENT_TYPE, WEBHOOK

class SubscriptionData(BaseModel):
    eventType: str = EVENT_TYPE
    webHookUrl: str = WEBHOOK
    enrollmentId: str = str(uuid.uuid4())