import json
import base64
from src.domain.repositories.bureau_logs_repository import BureauLogsRepository

class GetProspectEvaUseCase:
    def __init__(self, session):
        self.bureau_log_respository = BureauLogsRepository(session)


    def exec(self, id):
        try:
            response = self.bureau_log_respository.get_bureau_logs_by_prospect_id(id)
            decoded_bytes = base64.b64decode(response[0].encode('utf-8'))
            decoded_json = json.loads(decoded_bytes)
            return decoded_json
        except Exception as e:
            return str(e)
