# Local ALB-LAMBDA

This OSS project helps to mock an AWS ALB in local system for a serverless use case where an ALB invokes Lambda function. This component is an add on on-top of [LocalStack](https://github.com/localstack/localstack) which can be used to Mock Lambda in local system. 
Technical conepts are taken from [AWS ALB Developer Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)

![Design](alb-local-hld.png)

## Start local ALB
```console

docker-compose build

export TMPDIR=/private/var/folders/pn/vr3ntrm17rv0rwn55nxrbs9w0000gn/T/localstack

docker-compose up
```

## Deploy Hello Lambda & Test ALB
```console
cd flask/tests

python deploy-lambda-localstack.py

curl -i -d '{"first_name":"pepa", "last_name":"pig"}' -H "Content-Type: application/json" -X POST http://localhost:8080/alb/hello

python undeploy-lambda-localstack.py
```

## Miseleneous Commands

```console
python3 -m venv env

source env/bin/activate

pip3 install flask

pip3 list

pip3 freeze > requirement.txt


aws --endpoint-url=http://localhost:4566 lambda invoke \
    --function-name hello \
    --payload '{ "first_name": "pepa", "last_name":"pig"}' \
    response.json
```

