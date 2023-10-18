from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import desc

from src.infrastructure.data_sources.models.subscriptions_model import CirculoCreditoSubscription


class CirculoCreditoSubscriptionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, uuid: str):
        created_at = datetime.utcnow()
        subscription = CirculoCreditoSubscription(uuid=uuid, created_at=created_at)
        self.session.add(subscription)
        self.session.commit()
        return subscription

    def get_by_id(self, subscription_id: int):
        return self.session.query(CirculoCreditoSubscription).filter_by(id=subscription_id).first()

    def get_by_uuid(self, uuid: str):
        return self.session.query(CirculoCreditoSubscription).filter_by(uuid=uuid).first()

    def update(self, subscription: CirculoCreditoSubscription):
        self.session.commit()

    def delete(self, subscription: CirculoCreditoSubscription):
        self.session.delete(subscription)
        self.session.commit()

    def delete_by_uuid(self, uuid: str):
        subscription = self.get_by_uuid(uuid)
        if subscription:
            self.session.delete(subscription)
            self.session.commit()
            return True
        return False

    def get_latest_subscription(self):
        latest_subscription = self.session.query(CirculoCreditoSubscription).order_by(
            desc(CirculoCreditoSubscription.created_at)).first()
        if latest_subscription:
            return {
                "uuid": latest_subscription.uuid,
                "created_at": latest_subscription.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            return {}
