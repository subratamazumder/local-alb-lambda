from alb import app
from alb import lambda_invoker
from flask import request
@app.route('/')
def root_endpoint():
    return "root endpoint"

@app.route('/alb/<lambda_function_name>',methods=['POST'])
def alb_endpoint(lambda_function_name):
   return lambda_invoker.invoke(lambda_function_name,request.get_json())