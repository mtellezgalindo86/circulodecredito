from pydantic import BaseModel


class FullName(BaseModel):
    firstName: str
    middleName: str = None
    firstSurname: str
    secondSurname: str
    aditionalSurname: str = None


class Address(BaseModel):
    streetAndNumber: str
    settlement: str
    county: str
    city: str
    state: str
    postalCode: str


class PrivacyNotice(BaseModel):
    fullName: FullName
    address: Address
    acceptanceDate: str
    acceptance: str


class EmploymentVerification(BaseModel):
    employmentVerificationRequestId: str
    subscriptionId: str
    curp: str
    email: str
    dataProvider: str


class RequestData(BaseModel):
    privacyNotice: PrivacyNotice
    employmentVerification: EmploymentVerification
