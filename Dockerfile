FROM python:3

WORKDIR /usr/src/app

COPY requirements ./
COPY tox.ini ./
RUN pip install --no-cache-dir -r requirements

COPY ./src/ ./

CMD python3 quoridor.py
