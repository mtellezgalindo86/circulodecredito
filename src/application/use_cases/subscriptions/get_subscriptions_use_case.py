from src.application.services.subscriptions.get_subscriptions_service import GetSubscriptionsService

class GetSubscriptionsUseCase:
    def __init__(self):
        self.get_subscriptions = GetSubscriptionsService()

    def execute(self):
        try:
            response = self.get_subscriptions.get_subscritions()
            return response 
        except Exception as e:
            return str(e)
