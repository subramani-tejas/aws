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
import uuid

GET_RAW_PATH = "/getPerson"
CREATE_RAW_PATH = "/createPerson"


def lambda_handler(event, context):

    print(event)

    if event['rawPath'] == GET_RAW_PATH:
        # GET logic
        personID = event['queryStringParameters']['personID']
        insideRequest = event['requestContext']['http']['userAgent']
        return {
            "name": "tejas",
            "ID": personID,
            "insideRequest": insideRequest
        }

    elif event['rawPath'] == CREATE_RAW_PATH:
        # POST logic | write to DynamoDB?
        decodedEvent = json.loads(event['body'])
        return {
            "status": "ok from POST",
            "decodedEvent_Name": decodedEvent['name'],
            "decodedEvent_Age": decodedEvent['age'],
        }
