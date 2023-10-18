import requests
import logging
import json

from src.infrastructure.config.contants import HEADERS, BASE_URL
from src.domain.entities.eva.eva_authoritazion import Acknowledgement
from src.domain.entities.errors.errors import ErrorResponse
from src.domain.entities.eva.eva_inquiry_id import RequestDataIquiryId


class evaExternalImssClient:

    def __init__(self):
        self.base_url = BASE_URL

    def creatEvaAuthorization(self, data):

        try:
            url = f"{BASE_URL}/v1/eva/employmentverifications/withPrivacyNotice"
            data = data.dict()
            response = requests.post(url, headers=HEADERS, json=data)
            if response.status_code == 200:
                return Acknowledgement(**response.json())
            else:
                error_data = ErrorResponse(**response.json())
                logging.warning(f"Request failed with status code {response.status_code}. Error data: {error_data}")
                return error_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {str(e)}")
            return str(e)
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {str(e)}")
            return str(e)

    def getEvaInquiryId(self, employmentId):
        try:
            url = f"{BASE_URL}/v1/eva/employmentverifications/{employmentId}"
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                return RequestDataIquiryId(**response.json())
            else:
                error_data = ErrorResponse(**response.json())
                logging.warning(f"Request failed with status code {response.status_code}. Error data: {error_data}")
                return error_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {str(e)}")
            return str(e)
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {str(e)}")
            return str(e)
