from src.application.services.subscriptions.create_subscription_service import CreateSubscriptionService
from src.domain.repositories.subscriptions_repository import CirculoCreditoSubscriptionRepository
class CreateSubscriptionUseCase:
    def __init__(self, session):
        self.create_subscription_service = CreateSubscriptionService()
        self.subscription_repository = CirculoCreditoSubscriptionRepository(session)

    def execute(self, subscription_data):
        try:
            response = self.create_subscription_service.create_subscription(subscription_data)
            self.subscription_repository.create(response.subscription.subscriptionId)
            return response  
        except Exception as e:
            print(e)
            return str(e)
    