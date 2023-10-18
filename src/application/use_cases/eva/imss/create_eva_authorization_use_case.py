from src.application.services.eva.imss.create_eva_authorization_service import createEvaAuthorizationService
from src.domain.repositories.bureau_logs_repository import BureauLogsRepository


class createEvaAuthorizationUseCase:

    def __init__(self, session):
        self.create_eva_authorization = createEvaAuthorizationService()
        self.bureau_log_respository = BureauLogsRepository(session)

    def execute(self, data, prospect_id):
        try:
            print("use_case")
            response = self.create_eva_authorization.creatEvaAuthorization(data)
            response_json = response.dict()
            inquiry_id = response_json.get("inquiryId")
            self.bureau_log_respository.update_inquiryid_by_prospect_id(prospect_id, inquiry_id)
            return response
        except Exception as e:
            return str(e)
