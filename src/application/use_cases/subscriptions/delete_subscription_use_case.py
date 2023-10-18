from src.application.services.subscriptions.delete_subscription_service import DeleteSubscription
from src.domain.repositories.subscriptions_repository import CirculoCreditoSubscriptionRepository

class DeleteSubscriptionUseCase:
    def __init__(self, session):
        self.delete_subscription = DeleteSubscription()
        self.subscription_repository = CirculoCreditoSubscriptionRepository(session)

    def execute(self, id):
        try:
            response = self.delete_subscription.delete_subscription(id)
            self.subscription_repository.delete_by_uuid(id)
            return response 
        except Exception as e:
            return str(e)