import json
from src.application.use_cases.prospect.get_prospect_eva_use_case import GetProspectEvaUseCase
from src.infrastructure.config.logging import logger
from src.infrastructure.config.database import create_session


def handler(event, context):
    try:
        session = create_session()
        id = event["pathParameters"]["id"]
        get_potential_eva = GetProspectEvaUseCase(session)
        response = get_potential_eva.exec(id)
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
