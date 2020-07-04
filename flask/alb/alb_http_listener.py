from alb import app
from alb import alb_lambda_invoker, alb_payload_utils
from flask import request
@app.route('/')
def root_endpoint():
    return "root endpoint"


@app.route('/alb/<lambda_function_name>', methods=['POST'])
def alb_endpoint(lambda_function_name):
    print(request.get_json())
    print("Processing ALB request")
    return alb_payload_utils.prepare_alb_response(alb_lambda_invoker.invoke(lambda_function_name,
                                                                            alb_payload_utils.prepare_lambda_request(request)))
