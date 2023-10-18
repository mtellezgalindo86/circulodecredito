import json
from src.infrastructure.config.logging import logger
from src.application.use_cases.subscriptions.get_subscription_db_use_case import GetSubscriptionDbUseCase
from src.infrastructure.config.database import create_session


def handler(event, context):
    try:
        session = create_session()
        get_subscription_use_case = GetSubscriptionDbUseCase(session)
        response = get_subscription_use_case.execute()
        response_json = json.dumps(response)
        headers = {
            "Content-Type": "application/json"
        }
        return {
            "statusCode": 200,
            "body": response_json,
            "headers": headers
        }
    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor"})
        }
