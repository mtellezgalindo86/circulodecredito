import json
from src.application.use_cases.eva.imss.get_eva_inquiry_id_use_case import GetEvaInquiryIdUseCase
from src.infrastructure.config.logging import logger
from src.infrastructure.config.database import create_session


def handler(event, context):
    try:
        session = create_session()
        id = event["pathParameters"]["id"]
        get_eva_inquiry_id = GetEvaInquiryIdUseCase(session)
        response = get_eva_inquiry_id.execute(id)
        return {
            "statusCode": 200,
            "body": response.dict()
        }
    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor"})
        }
