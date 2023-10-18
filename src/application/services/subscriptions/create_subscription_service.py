from src.infrastructure.external.api_clients.circulo_credito.subscriptions.subscriptions_client import \
    SubscriptionsClient


class CreateSubscriptionService:
    def __init__(self):
        self.subscriptions_client = SubscriptionsClient()

    def create_subscription(self, subscription_data):
        if not subscription_data:
            raise ValueError("Los datos de la suscripción son requeridos.")

        response = self.subscriptions_client.create_subscription(subscription_data)
        return response
