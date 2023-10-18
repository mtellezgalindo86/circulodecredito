import json
from src.application.use_cases.subscriptions.create_subscription_use_case import CreateSubscriptionUseCase
from src.domain.entities.subscriptions.subscription import SubscriptionData
from src.infrastructure.config.logging import logger
from src.infrastructure.config.database import create_session
from src.domain.entities.errors.errors import ErrorResponse


def handler(event, context):
    try:
        session = create_session()
        subscription_data = SubscriptionData()
        create_subscription_use_case = CreateSubscriptionUseCase(session)
        created_subscription = create_subscription_use_case.execute(subscription_data)
        headers = {
            "Content-Type": "application/json"
        }

        session.close()
        if isinstance(created_subscription,ErrorResponse):
            return {
                "statusCode": 400,
                "body": json.dumps(created_subscription.dict()),
                "headers": headers
            }
        
        return {
            "statusCode": 200,
            "body": json.dumps(created_subscription.dict()),
            "headers": headers
        }
    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor"})
        }
