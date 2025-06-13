FROM python:3.13.5-alpine
COPY run_server.py requerements.txt /app/
RUN apk add --update --no-cache gcc musl-dev libffi-dev openssl-dev && \
    rm -rf /var/cache/apk/* && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requerements.txt && \
    pip cache purge
ENTRYPOINT python /app/run_server.py --ip $IP --port 8000 --token $TOKEN
