import base64
import json
from src.application.services.eva.imss.get_eva_inquiry_id_service import getEvaInquiryIdService
from src.domain.repositories.bureau_logs_repository import BureauLogsRepository


class GetEvaInquiryIdUseCase:
    def __init__(self, session):
        self.get_eva_inquiry_id = getEvaInquiryIdService()
        self.bureau_log_repository = BureauLogsRepository(session)

    def execute(self, data):
        try:
            # Verificar si existe un registro de log
            if not self.bureau_log_repository.bureau_log_exists(data):
                return None  # Puedes manejar la falta de registro de log según tus necesidades

            # Obtener la respuesta de getEvaInquiryId
            response = self.get_eva_inquiry_id.getEvaInquiryId(data)
            print("obteniendo informacion del id", response)
            # Codificar la respuesta en base64
            encoded_response = base64.b64encode(json.dumps(response.dict()).encode('utf-8')).decode('utf-8')
            print("se codifica la respuesta en base64")
            # Actualizar el registro de log con la respuesta codificada
            self.bureau_log_repository.update_circulo_credito_response(data, encoded_response)
            print("se actualiza el registro de log con la respuesta codificada")
            return response
        except Exception as e:
            return str(e)
