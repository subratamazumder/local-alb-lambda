import json
import os
import boto3
from botocore.config import Config

CONFIG = Config(connect_timeout=10, read_timeout=10,
                retries={'max_attempts': 0})
LOCALSTACK_ENDPOINT = os.environ['LOCALSTACK_ENDPOINT']


def get_lambda_client():
    print("Connecting to local stack running on {}".format(LOCALSTACK_ENDPOINT))
    return boto3.client(
        'lambda',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='',
        endpoint_url=LOCALSTACK_ENDPOINT,
        config=CONFIG
    )


def invoke(function_name='function1', function_payload='{"hello":"hello"}', invocation_type='RequestResponse'):
    response = ''
    print("Lambda {} invoked with".format(function_name))
    print(json.dumps(function_payload, indent=4, sort_keys=True))
    lambda_client = get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType=invocation_type,
        Payload=json.dumps(function_payload)
    )
    lambda_payload_response = json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )
    print("\r\nLambda response paylaod")
    print(json.dumps(lambda_payload_response, indent=4, sort_keys=True))
    return lambda_payload_response
