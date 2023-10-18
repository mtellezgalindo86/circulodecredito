import boto3
from src.infrastructure.config.contants import URL_SQS


class SQSClient:
    def __init__(self, region_name='us-east-1'):
        self.client = boto3.client('sqs', region_name=region_name)
        self.queue_url = URL_SQS

    def send_message(self, message_body, group):
        response = self.client.send_message(QueueUrl=self.queue_url, MessageBody=message_body, MessageGroupId=group)
        return response

    def receive_message(self):
        response = self.client.receive_message(QueueUrl=self.queue_url)
        return response

    def delete_message(self, receipt_handle):
        self.client.delete_message(QueueUrl=self.queue_url, ReceiptHandle=receipt_handle)
