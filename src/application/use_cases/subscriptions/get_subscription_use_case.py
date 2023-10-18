from src.application.services.subscriptions.get_subscription_service import GetSubscriptionService

class GetSubscriptionUseCase:
    def __init__(self):
        self.get_subscription = GetSubscriptionService()

    def execute(self, id):
        try:
            response = self.get_subscription.get_subscription_by_id(id)
            return response
        except Exception as e:
            return str(e)