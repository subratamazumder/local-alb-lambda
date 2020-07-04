# Local ALB-LAMBDA

This OSS project help to mock a ALB in a serverless use case where an ALB invokes Lambda function which is mocked by [LocalStack](https://github.com/localstack/localstack).

## Start local ALB
```console

docker-compose build

export TMPDIR=/private/var/folders/pn/vr3ntrm17rv0rwn55nxrbs9w0000gn/T/localstack

docker-compose up
```

## Deploy Hello Lambda & Test ALB
```console
cd flask/tests

python3 test.py
```

## Test ALB via cURL

```console
curl -i -d '{"first_name":"pepa", "last_name":"pig"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/alb/hello
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

