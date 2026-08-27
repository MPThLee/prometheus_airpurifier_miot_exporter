FROM python:3.12-slim-bookworm AS builder
COPY requirements.txt /build/
RUN apt-get update && \
    apt-get install --yes --no-install-recommends build-essential && \
    pip wheel --no-cache-dir --wheel-dir /wheels -r /build/requirements.txt

FROM python:3.12-slim-bookworm
COPY --from=builder /wheels /wheels
COPY run_server.py /app/
RUN pip install --no-cache-dir /wheels/* && \
    python -c "from miio import AirPurifierMiot" && \
    rm -rf /wheels
ENTRYPOINT ["/bin/sh", "-c", "python /app/run_server.py --ip $IP --port 8000 --token $TOKEN"]
