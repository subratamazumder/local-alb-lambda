import json
from json import JSONEncoder
import os
import boto3
from botocore.config import Config

CONFIG = Config(connect_timeout=10, read_timeout=10,
                retries={'max_attempts': 0})
LOCALSTACK_ENDPOINT = os.getenv('LOCALSTACK_ENDPOINT', 'http://localhost:4566')

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
class CustomSetEncoder(JSONEncoder):
        def default(self, obj):
            return list(obj)

def invoke(function_name='function1', function_payload='{"hello":"hello"}', invocation_type='RequestResponse'):
    response = ''
    print(type(function_payload))
    print("Lambda {} invoked with".format(function_name))
    print(json.dumps(function_payload, indent=4, sort_keys=True, cls=CustomSetEncoder))
    lambda_client = get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType=invocation_type,
        Payload=json.dumps(function_payload,cls=CustomSetEncoder)
    )
    lambda_payload_response = json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )
    print("\r\nLambda response paylaod")
    print(json.dumps(lambda_payload_response, indent=4, sort_keys=True))
    return lambda_payload_response
