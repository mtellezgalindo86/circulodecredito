import json
import uuid
import base64
from src.infrastructure.config.contants import SECRET_KEY
from src.infrastructure.config.logging import logger
from src.infrastructure.config.sqs.sqs_client import SQSClient
from src.application.use_cases.eva.imss.get_eva_inquiry_id_use_case import GetEvaInquiryIdUseCase
from src.application.use_cases.eva.issste.get_eva_inquiry_id_use_case import GetEvaInquiryIsssteIdUseCase
from src.application.use_cases.prospect.get_validate_issste import GetProspectValidateUseCase
from src.infrastructure.config.database import create_session


def handler(event, context):
    try:
        print(event)

        # Extraer el cuerpo del mensaje del evento
        event_body = event.get('body', None)
        if not event_body:
            raise ValueError("El evento no contiene un cuerpo válido.")

        request_body = json.loads(event_body)

        # Generar un ID de deduplicación único para el mensaje
        message_deduplication_id = str(uuid.uuid4())

        # Crear una instancia de SQSClient
        sqs_client = SQSClient()

        # Enviar el mensaje a SQS
        response = sqs_client.send_message(json.dumps(request_body), message_deduplication_id)

        print(f"Mensaje enviado a SQS: {response}")

        return {
            'statusCode': 200,
            'body': 'Solicitud procesada y enviada a SQS con éxito'
        }
    except Exception as e:
        print(f"Error al procesar la solicitud: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'Error al procesar la solicitud'
        }


def processSQSMessage(event, context):
    # Verificar si hay registros en el evento SQS
    records = event.get("Records", [])
    if not records:
        print("No se encontraron registros en el evento SQS.")
        return False

    # Crear una sesión fuera del bucle para reutilizarla para todos los registros
    session = create_session()
    sqs_client = SQSClient()

    for record in records:
        # Obtener el cuerpo del mensaje SQS de cada registro
        sqs_message_body = record.get("body")
        if not sqs_message_body:
            print("No se encontró el cuerpo del mensaje SQS en un registro.")
            continue  # Saltar este registro y continuar con el siguiente

        try:
            body_data = json.loads(sqs_message_body)
            print("Cuerpo del mensaje JSON:", body_data)

            # Obtener el inquiryId del objeto JSON
            inquiry_id = body_data["inquiry"].get("inquiryId")
            if not inquiry_id:
                print("La clave 'inquiryId' no tiene un valor en el objeto JSON.")
                continue  # Saltar este registro y continuar con el siguiente

            get_validate_issste = GetProspectValidateUseCase(session)
            validate = get_validate_issste.exec(inquiry_id)
            if validate:
                print("el proceso es para issste")
                get_eva_issste_inquiry_id = GetEvaInquiryIsssteIdUseCase(session)
                responses = get_eva_issste_inquiry_id.execute(inquiry_id)
            else:
                # Obtener el resultado de la consulta
                get_eva_inquiry_id = GetEvaInquiryIdUseCase(session)
                responses = get_eva_inquiry_id.execute(inquiry_id)

            # Obtener el handle del registro para eliminarlo
            receipt_handle = record.get("receiptHandle")
            if receipt_handle:
                sqs_client.delete_message(receipt_handle)
                print("Mensaje eliminado de la cola.")

            # Continuar con el procesamiento de los datos según sea necesario
                

        except Exception as e:
            print("Error en el procesamiento del mensaje:", str(e))
            continue  # Saltar este registro y continuar con el siguiente
    session.close()
    # Si llega aquí, todos los registros han sido procesados exitosamente
    return {
        'statusCode': 200,
        'body': json.dumps('Todos los registros procesados y eliminados de la cola con éxito')
    }
