FROM python:3.11.1-slim

COPY requirements.txt ./app/requirements.txt

RUN pip install -r ./app/requirements.txt

COPY . /app

WORKDIR /app

CMD python main.py