from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, JSON, Boolean, Text

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BureauLogs(Base):
    __tablename__ = 'bureau_logs'

    id = Column(Integer, primary_key=True)
    prospect_id = Column(Integer)
    pre_approved_request_id = Column(Integer)
    response = Column(JSON)
    status = Column(String)
    request_id = Column(Integer)
    consultation_number = Column(String)
    available = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    consultation_control_number = Column(String)
    mop96 = Column(String)
    payload = Column(JSON)
    circulo_credito_response = Column(Text)
    inquiryid = Column(String)
    issste = Column(Boolean)
