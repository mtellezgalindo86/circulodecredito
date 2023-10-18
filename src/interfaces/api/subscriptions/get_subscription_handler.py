import json
from src.infrastructure.config.logging import logger
from src.application.use_cases.subscriptions.get_subscription_use_case import GetSubscriptionUseCase
from src.domain.entities.errors.errors import ErrorResponse


def handler(event, context):
    try:
        id = event["pathParameters"]["id"]
        get_subscription_use_case = GetSubscriptionUseCase()
        response = get_subscription_use_case.execute(id)
        response_dict = response.dict()  # Utiliza el método dict() de Pydantic
        headers = {
            "Content-Type": "application/json"
        }
        if isinstance(response_dict,ErrorResponse):
            return {
                "statusCode": 400,
                "body": json.dumps(response_dict.dict()),
                "headers": headers
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
