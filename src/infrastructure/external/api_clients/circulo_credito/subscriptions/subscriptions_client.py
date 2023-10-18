import requests
import logging

from src.infrastructure.config.contants import HEADERS, BASE_URL
from src.domain.entities.subscriptions.subscription_detail import SubscriptionDataDetail
from src.domain.entities.subscriptions.subscription_response import SubscriptionResponse
from src.domain.entities.subscriptions.subscription_list import SubscriptionResponseList
from src.domain.entities.errors.errors import ErrorResponse


class SubscriptionsClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_subscription(self, data):
        try:
            url = f"{self.base_url}/v1/subscriptions"
            data = data.dict()
            response = requests.post(url, headers=HEADERS, json=data)

            if response.status_code == 200:
                response_data = SubscriptionResponse(**response.json())
                logging.info(f"Request successful. Response data: {response_data}")
                return response_data
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

    def get_subscriptions(self):
        try:
            url = f"{self.base_url}/v1/subscriptions"
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                return SubscriptionResponseList(**response.json())
            else:
                error_data = response.json()
                logging.warning(f"Request failed with status code {response.status_code}. Error data: {error_data}")
                return error_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {str(e)}")
            return str(e)
        except Exception as e:
            logging.exception(f"An unexpected error courred:{str(e)}")
            return str(e)

    def get_subscription(self, id):
        try:
            url = f"{self.base_url}/v1/subscriptions/{id}"
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                response_data = SubscriptionDataDetail(**response.json())
                return response_data
            else:
                error_data = ErrorResponse(**response.json())
                logging.warning(f"Request failed with status code {response.status_code}. Error data: {error_data}")
                return error_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {str(e)}")
            return str(e)
        except Exception as e:
            logging.exception(f"An unexpected error courred:{str(e)}")
            return str(e)

    def delete_subscription(self, id):
        try:
            url = f"{self.base_url}/v1/subscriptions/{id}"
            response = requests.delete(url, headers=HEADERS)
            if response.status_code == 200:
                return response.json()
            else:
                error_data = response.json()
                logging.warning(f"Request failed with status code {response.status_code}. Error data: {error_data}")
                return error_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {str(e)}")
            return str(e)
        except Exception as e:
            logging.exception(f"An unexpected error courred:{str(e)}")
            return str(e)
