import json

def health_check(event, context):
    body = {
        "status": "healthy",
        "message": "Service is running smoothly",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response