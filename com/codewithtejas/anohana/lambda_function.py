# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=unused-import - W0611
# pylint: disable=inconsistent-return-statements - R1710
# pylint: disable=unused-argument - W0613
# pylint: disable=invalid-name - C0103

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
