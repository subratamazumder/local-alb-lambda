FROM python:3.7.5-stretch
WORKDIR /alb
ADD . /alb
RUN pip3 install -r requirement.txt
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]