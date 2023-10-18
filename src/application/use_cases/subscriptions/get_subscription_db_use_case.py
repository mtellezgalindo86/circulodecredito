from src.domain.repositories.subscriptions_repository import CirculoCreditoSubscriptionRepository

class GetSubscriptionDbUseCase:
    def __init__(self,session):
        self.get_subscription = CirculoCreditoSubscriptionRepository(session)

    def execute(self):
        try:
            response = self.get_subscription.get_latest_subscription()
            return response  
        except Exception as e:
            return str(e)