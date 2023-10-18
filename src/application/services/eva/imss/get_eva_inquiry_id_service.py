from src.infrastructure.external.api_clients.circulo_credito.eva.imss.external_api_client import evaExternalImssClient


class getEvaInquiryIdService:

    def __init__(self):
        self.eva_client = evaExternalImssClient()

    def getEvaInquiryId(self, data):
        if not data:
            raise ValueError("El id del empleado es requerido.")

        response = self.eva_client.getEvaInquiryId(data)
        return response
