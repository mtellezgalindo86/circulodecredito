from src.infrastructure.external.api_clients.circulo_credito.eva.issste.external_api_client import ExternalIsssteClient


class getEvaInquiryIdService:

    def __init__(self):
        self.eva_client = ExternalIsssteClient()

    def getEvaInquiryId(self, data):
        if not data:
            raise ValueError("El id del empleado es requerido.")

        response = self.eva_client.getInfoEmployment(data)
        return response
