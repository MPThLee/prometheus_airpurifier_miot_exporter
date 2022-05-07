FROM python:3.10-alpine
RUN apk add --update gcc musl-dev libffi-dev openssl-dev
COPY requerements.txt /app/
COPY run_server.py /app/
RUN pip install --upgrade pip && pip install -r /app/requerements.txt
ENTRYPOINT python /app/run_server.py --ip $IP --port 8000 --token $TOKEN
