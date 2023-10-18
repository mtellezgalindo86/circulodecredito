import json
from src.application.use_cases.eva.issste.create_eva_authorization_use_case import createEvaAuthorizationUseCase
from src.domain.entities.eva.eva_verification_notice import RequestData
from src.infrastructure.config.logging import logger
from src.infrastructure.config.database import create_session


def handler(event, context):
    try:
        session = create_session()
        request_body = json.loads(event['body'])
        prospect_id = request_body.get("prospect_id")
        new_request_body = request_body.copy()
        del new_request_body["prospect_id"]

        # Crear una instancia de RequestData
        request_data = RequestData(**new_request_body)
        create_eva_authorization = createEvaAuthorizationUseCase(session)
        response = create_eva_authorization.execute(request_data, prospect_id)
        headers = {
            "Content-Type": "application/json"
        }
        return {
            "statusCode": 200,
            "body": json.dumps(response.dict()),
            "headers": headers
        }
    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor"})
        }
