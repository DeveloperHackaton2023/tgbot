FROM python:3.11-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY bot bot

CMD python bot/main.py
