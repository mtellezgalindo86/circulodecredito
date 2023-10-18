import json
from src.infrastructure.config.logging import logger
from src.application.use_cases.subscriptions.delete_subscription_use_case import DeleteSubscriptionUseCase
from src.infrastructure.config.database import create_session


def handler(event, context):
    try:
        session = create_session()
        id = event["pathParameters"]["id"]
        delete_subscription_use_case = DeleteSubscriptionUseCase(session)
        response = delete_subscription_use_case.execute(id)
        headers = {
            "Content-Type": "application/json"
        }
        return {
            "statusCode": 200,
            "body": json.dumps(response),
            "headers": headers

        }
    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor"})
        }
