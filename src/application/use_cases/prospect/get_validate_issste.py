import json
import base64
from src.domain.repositories.bureau_logs_repository import BureauLogsRepository


class GetProspectValidateUseCase:
    def __init__(self, session):
        self.bureau_log_respository = BureauLogsRepository(session)

    def exec(self, id):
        try:
            response = self.bureau_log_respository.is_issste(id)
            return response
        except Exception as e:
            return str(e)
