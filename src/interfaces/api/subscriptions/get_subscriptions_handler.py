import json
from src.infrastructure.config.logging import logger
from src.application.use_cases.subscriptions.get_subscriptions_use_case import GetSubscriptionsUseCase


def handler(event, context):
    try:
        get_subscriptions_use_case = GetSubscriptionsUseCase()
        response = get_subscriptions_use_case.execute()
        response_dict = response.dict()
        headers = {
            "Content-Type": "application/json"
        }
        return {
            "statusCode": 200,
            "body": json.dumps(response_dict),
            "headers": headers
        }
    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor"})
        }
