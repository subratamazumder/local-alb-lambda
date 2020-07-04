# A container based solution to mock ALB-LAMBDA scenario in local

python3 -m venv env

source env/bin/activate

pip3 install flask

pip3 list

pip3 freeze > requirement.txt

docker-compose config

docker-compose build

docker-compose up


docker run -it -e DEBUG=1 -e DEFAULT_REGION="us-east-1" -e TEST_AWS_ACCOUNT_ID="000000000000" -e SERVICES="lambda,cloudwatch" -e LOCALSTACK_HOSTNAME="localhost" -e LAMBDA_EXECUTOR="docker" -p 4566:4566 --rm --privileged --name localstack_main -v "/private/var/folders/pn/vr3ntrm17rv0rwn55nxrbs9w0000gn/T/localstack:/tmp/localstack" -v "/var/run/docker.sock:/var/run/docker.sock" -e DOCKER_HOST="unix:///var/run/docker.sock" --net-alias "localstack" --net "bridge" "localstack/localstack"

Deploy Hello Lambda
tests/test.py

Test ALB 

curl -i -d '{"first_name":"pepa", "last_name":"pig"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/alb/hello

Test Lambda

aws --endpoint-url=http://localhost:4566 lambda invoke \
    --function-name hello \
    --payload '{ "first_name": "pepa", "last_name":"pig"}' \
    response.json

    LOCALSTACK_ENDPOINT = 'http://localhost:4566'

