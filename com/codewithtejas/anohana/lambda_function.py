# pylint: disable-all

import json
import boto3
from botocore.exceptions import ClientError

GET_path = "/anohana_LF/getDetails"
POST_path = "/anohana_LF/postDetails"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('anohana_DB')


def lambda_handler(event, context):

    # GET logic | get all from DynamoDB
    if event['rawPath'] == GET_path:
        try:
            response = table.scan()
        except ClientError as e:
            print(e.response['Error']['Message'])

        return response['Items']

    # POST logic | add item to DynamoDB
    elif event['rawPath'] == POST_path:
        try:
            decodedEvent = json.loads(event['body'])
            table.put_item(Item=decodedEvent)
        except ClientError as e:
            print(e.response['Error']['Message'])

        return {
            "status_code": "200",
            "text": "Added!"
        }
