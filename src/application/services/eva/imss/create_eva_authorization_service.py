from src.infrastructure.external.api_clients.circulo_credito.eva.imss.external_api_client import evaExternalImssClient


class createEvaAuthorizationService:

    def __init__(self):
        self.eva_client = evaExternalImssClient()

    def creatEvaAuthorization(self, data):
        if not data:
            raise ValueError("Los datos de la suscripción son requeridos.")

        response = self.eva_client.creatEvaAuthorization(data)
        return response
