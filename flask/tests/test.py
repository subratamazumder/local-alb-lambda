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
FUNCTION_NAME='hello1'

def get_lambda_client():
    return boto3.client(
        'lambda',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='eu-west-2',
        endpoint_url=LOCALSTACK_ENDPOINT,
        config=CONFIG
    )


def create_lambda_zip(function_name):
    with ZipFile(LAMBDA_ZIP, 'w') as z:
        z.write('lambda' + '.py')


def create_lambda(function_name):
    lambda_client = get_lambda_client()
    create_lambda_zip(function_name)
    with open(LAMBDA_ZIP, 'rb') as f:
        zipped_code = f.read()
    lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.7',
        Role='role',
        Timeout=10,
        Handler='lambda.lambda_handler',
        Code=dict(ZipFile=zipped_code),
    )
    print("Lambda created")


def delete_lambda(function_name):
    lambda_client = get_lambda_client()
    lambda_client.delete_function(
        FunctionName=function_name
    )
    os.remove(LAMBDA_ZIP)
    print("Lambda deleted")
def invoke_fake_alb(function_name='hello', body = {"first_name": "value1", "last_name": "value2"}):
    
    myurl = "http://localhost:8080/alb/{}".format(function_name)
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print(jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    print(json.load(response))
try:
    create_lambda(FUNCTION_NAME)
    invoke_fake_alb(FUNCTION_NAME)
except Exception as e:
    delete_lambda(FUNCTION_NAME)

