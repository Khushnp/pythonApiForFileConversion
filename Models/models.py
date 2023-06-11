from datetime import date
from pydantic import BaseModel
from typing import List, Optional

class Customer(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    bankUserId: Optional[str]
    countyCode: Optional[str]
    birthDate: Optional[date]
    cityOfBirth: Optional[str]
    EID: Optional[str]
    NID: Optional[str]
    passport: Optional[str]
    economicActivityCode: Optional[str]
    documentIssuerCountryCode: Optional[str]
    documentType: Optional[str]

class Proxy(BaseModel):
    type: Optional[str]
    value: Optional[str]

class CustomerBankaccount(BaseModel):
    IBAN: Optional[str]
    currency: Optional[str]
    accountType: Optional[str]

class CustomerBulkUploadBody(BaseModel):
    operationType: Optional[str]
    customer: Optional[Customer]
    mobile: Optional[str]
    bankAccount: Optional[List[CustomerBankaccount]]
    proxies: Optional[List[Proxy]]

class BulkOperationHeader(BaseModel):
    groupCode: Optional[str]
    bankCode: Optional[str]    
    recordNumber: Optional[int]
    date: Optional[str]
    fileNumber: Optional[str]
    operationType: Optional[str]
    
