# Prometheus exporter for Xiaomi Air Purifier MIOT Varient

![Grafana Dashboard](img/grafana.png)

## Get device token
Use instructions: [https://github.com/jghaanstra/com.xiaomi-miio/blob/master/docs/obtain_token.md](https://github.com/jghaanstra/com.xiaomi-miio/blob/master/docs/obtain_token.md)

Or just install patched app: [http://www.kapiba.ru/2017/11/mi-home.html](http://www.kapiba.ru/2017/11/mi-home.html)

## `--model` Argument.
Use `--model` argument for pass unsupported model treat as another model.

ex) Air Purifier 4 with `--model zhimi.airp.va2` (Air Purifier 4 Pro. It completely compatible but miio 0.5.x supports only 4 Pro.)

## Run with Docker
```bash
docker run -d --name prometheus_humidifier -p 8000:8000 -e "TOKEN=xxxxxxxx" -e "IP=xx.xx.xx.xx" ghcr.io/MPThLee/prometheus_airpurifier_miot_exporter
```
Doesn't work with `--model` argument.

## Container registry
![Build](https://github.com/MPThLee/prometheus_airpurifier_miot_exporter/actions/workflows/build-docker.yml/badge.svg)

[https://ghcr.io/MPThLee/prometheus_airpurifier_miot_exporter](https://ghcr.io/MPThLee/prometheus_airpurifier_miot_exporter)
