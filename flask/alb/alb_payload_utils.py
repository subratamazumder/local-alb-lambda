import json
from flask import request

# TODO : Path handling, instead of taking function name from path, should take from env var
def prepare_lambda_request(request):
    return convert_to_lambda_request(request.get_json(), request.method, request.query_string, request.content_type, request.accept_mimetypes)


def convert_to_lambda_request(alb_req_body='', alb_req_method='GET', alb_req_params='', alb_req_body_content_type='application/json', alb_accept_content_type='application/json'):
    return {
        "requestContext": {
            "elb": {
                "targetGroupArn": "arn:aws:elasticloadbalancing:region:000000000000:targetgroup/my-target-group/6d0ecf831eec9f09"
            }
        },
        "httpMethod": alb_req_method,
        "path": "/",
        "queryStringParameters": {alb_req_params},
        "headers": {
            "accept": alb_accept_content_type,
            "accept-language": "en-US,en;q=0.8",
            "content-type": alb_req_body_content_type,
            "cookie": "cookies",
            "host": "lambda-846800462-us-east-2.elb.amazonaws.com",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)",
            "x-amzn-trace-id": "Root=1-5bdb40ca-556d8b0c50dc66f0511bf520",
            "x-forwarded-for": "00.00.000.00",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "isBase64Encoded": False,
        "body": json.dumps(alb_req_body)
    }

# TODO : Extract body, header & response code
def prepare_alb_response(lambda_response):
    print(type(lambda_response))
    return lambda_response

