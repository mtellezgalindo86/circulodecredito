from typing import List, Optional
from pydantic import BaseModel


class EmploymentStatusEvent(BaseModel):
    changeType: int
    eventDate: str
    baseSalary: str


class EmploymentHistoryDetail(BaseModel):
    employerName: str
    employerRegister: str
    federalEntity: str
    startDate: str
    endDate: str
    lastContributionBaseSalary: int
    workStatusEvents: List[EmploymentStatusEvent]


class WorkingHistory(BaseModel):
    date: str
    weeksContributed: Optional[dict]  # Optional field
    workingHistoryDetail: List[EmploymentHistoryDetail]


class EmploymentVerificationRequest(BaseModel):
    employmentVerificationRequestId: str
    subscriptionId: str
    inquiryId: str
    curp: str
    email: str
    inquiryStatus: str
    successCheck: Optional[bool]  # Optional field


class EmploymentVerification(BaseModel):
    request: EmploymentVerificationRequest
    names: Optional[str]  # Optional field
    birthday: Optional[str]  # Optional field
    workStatus: Optional[str]  # Optional field
    nssCheck: Optional[bool]  # Optional field
    workingHistory: Optional[WorkingHistory]  # Optional field
    validUntil: Optional[str]  # Optional field


class Acknowledgement(BaseModel):
    acknowledgeId: str
    dateTime: str
    operation: str
    message: str
    employmentVerification: Optional[EmploymentVerification]  # Optional field


class RequestDataIquiryId(BaseModel):
    acknowledgeId: str
    dateTime: str
    operation: str
    message: str
    employmentVerification: Optional[EmploymentVerification]  # Optional field
