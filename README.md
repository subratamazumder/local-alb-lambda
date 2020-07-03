# A container based solution to mock ALB-LAMBDA scenario in local

python3 -m venv env

source env/bin/activate

pip3 install flask

pip3 list

pip3 freeze > requirement.txt

docker-compose config

docker-compose build

docker-compose up

curl -i -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080/alb/function1

