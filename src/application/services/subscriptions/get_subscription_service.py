from src.infrastructure.external.api_clients.circulo_credito.subscriptions.subscriptions_client import \
    SubscriptionsClient
from src.infrastructure.config.logging import logger


class GetSubscriptionService:
    def __init__(self):
        self.subscriptions_client = SubscriptionsClient()

    def get_subscription_by_id(self, id):
        if not id:
            logger.info("El id de la suscripción es requerido")
            raise ValueError("El id de la suscripción es requerido.")

        response = self.subscriptions_client.get_subscription(id)
        return response
