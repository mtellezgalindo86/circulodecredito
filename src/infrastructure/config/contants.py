import os


HEADERS = {
    'Content-Type': 'application/json',
    'x-api-key': os.environ.get("API_KEY")
}

BASE_URL = os.environ.get("BASE_URL")
EVENT_TYPE = os.environ.get("eventType")
WEBHOOK = os.environ.get("webhookUrl")

DB_URL = os.environ.get("HOST")
DB_USER= os.environ.get("USER")
DB_PASSWORD=os.environ.get("PASSWORD")
DB_DATABASE=os.environ.get("DB")
DB_CONNECTION = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB_DATABASE}"
URL_SQS = os.environ.get("SQS_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")