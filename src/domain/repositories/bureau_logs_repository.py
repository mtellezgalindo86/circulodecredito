from sqlalchemy.orm import Session
from src.infrastructure.data_sources.models.bureau_logs import BureauLogs


class BureauLogsRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_bureau_log(self, prospect_id: int, inquiryid: str, circulo_credito_response: str):
        new_log = BureauLogs(prospect_id=prospect_id, inquiryid=inquiryid,
                             circulo_credito_response=circulo_credito_response)
        self.session.add(new_log)
        self.session.commit()

    def get_bureau_logs_by_prospect_id(self, prospect_id: int):
        results = self.session.query(BureauLogs.circulo_credito_response).filter_by(prospect_id=prospect_id).first()
        return results

    def update_circulo_credito_response(self, inquiryid: str, circulo_credito_response: str):
        bureau_log = self.session.query(BureauLogs).filter_by(inquiryid=inquiryid).first()
        if bureau_log:
            bureau_log.circulo_credito_response = circulo_credito_response
            self.session.commit()

    def bureau_log_exists(self, inquiryid: str):
        return self.session.query(BureauLogs).filter_by(inquiryid=inquiryid).first() is not None

    def update_inquiryid_by_prospect_id(self, prospect_id: int, new_inquiryid: str):
        bureau_log = self.session.query(BureauLogs).filter_by(prospect_id=prospect_id).first()
        if bureau_log:
            bureau_log.inquiryid = new_inquiryid
            self.session.commit()

    def update_inquiry_id_issste(self, project_id: int, new_inquiryid: str, issste:bool):
        bureau_log = self.session.query(BureauLogs).filter_by(prospect_id=project_id).first()
        if bureau_log:
            bureau_log.inquiryid = new_inquiryid
            bureau_log.issste = issste
            self.session.commit()

    def is_issste(self, inquiryid: str):
        bureau_log = self.session.query(BureauLogs).filter_by(inquiryid=inquiryid).first()
        if bureau_log:
            return bureau_log.issste
        else:
            return None
