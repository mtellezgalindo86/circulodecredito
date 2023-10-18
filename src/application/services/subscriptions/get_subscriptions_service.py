from src.infrastructure.external.api_clients.circulo_credito.subscriptions.subscriptions_client import \
    SubscriptionsClient
from src.infrastructure.config.logging import logger


class GetSubscriptionsService:
    def __init__(self):
        self.subscriptions_client = SubscriptionsClient()

    def get_subscritions(self):
        try:
            response = self.subscriptions_client.get_subscriptions()
            return response
        except Exception as e:
            logger.exception(f"An unexpected error occurred: {str(e)}")
            return str(e)
