FROM python:3.11.2

WORKDIR /usr/src/pyapp

COPY trigger.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "trigger.py" ]
