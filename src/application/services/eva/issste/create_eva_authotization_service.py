from src.infrastructure.external.api_clients.circulo_credito.eva.issste.external_api_client import ExternalIsssteClient


class createEvaAuthorizationService:

    def __init__(self):
        self.eva_client = ExternalIsssteClient()

    def creatEvaAuthorization(self, data):
        if not data:
            raise ValueError("Los datos de la suscripción son requeridos.")

        response = self.eva_client.evPrivacyNotice(data)
        return response
