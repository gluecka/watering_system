FROM python:3.11.2

WORKDIR /usr/src/pyapp

COPY soil_value_ident.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "soil_value_ident.py" ]
