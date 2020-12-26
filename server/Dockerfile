FROM python:3.7-slim-buster

WORKDIR /app

COPY pip-packages.txt ./

RUN pip install -r pip-packages.txt

COPY ./src/. .

CMD [ "python3", "-u", "./main.py" ]
