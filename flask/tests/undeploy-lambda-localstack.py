import json
import os
from zipfile import ZipFile
import boto3
import botocore
from botocore.config import Config
import urllib

config = Config(connect_timeout=10, read_timeout=10)

CONFIG = botocore.config.Config(retries={'max_attempts': 0})
LAMBDA_ZIP = './lambda.zip'
LOCALSTACK_ENDPOINT = 'http://localhost:4566'
FUNCTION_NAME='hello'  

def get_lambda_client():
    return boto3.client(
        'lambda',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='eu-west-2',
        endpoint_url=LOCALSTACK_ENDPOINT,
        config=CONFIG
    )

def delete_lambda(function_name):
    lambda_client = get_lambda_client()
    lambda_client.delete_function(
        FunctionName=function_name
    )
    os.remove(LAMBDA_ZIP)
    print("Lambda deleted")

try:
    delete_lambda(FUNCTION_NAME)
except Exception as e:
    print('failed to undeploy lambda')

