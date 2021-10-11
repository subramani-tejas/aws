# pylint: disable-all

import json
import boto3

sqs = boto3.client('sqs', region_name='us-east-1')
POST_path = "/postDetails"


def lambda_handler(event, context):
    """
    look for a queue named pleure_queue
    my_queues = sqs.list_queues(QueueNamePrefix='pleure')
    sqs.list_queues --> returns this:
    {
        "QueueUrls": [
        "https://queue.amazonaws.com/028415855669/test_queue"
        ],
        "ResponseMetadata": {
            "RequestId": "a757c0f1-2d6b-51ac-a138-992c8682a077",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid": "a757c0f1-2d6b-51ac-a138-992c8682a077",
                "date": "Mon, 11 Oct 2021 03:04:09 GMT",
                "content-type": "text/xml",
                "content-length": "318"
            },
            "RetryAttempts": 0
        }
    }
    """

    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/028415855669/pleure_queue",
        MessageBody='message to the queue'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
