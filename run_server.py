#! /usr/bin/env python3
from miio import airpurifier_miot
from prometheus_client import Gauge
import prometheus_client
import logging
import time
import argparse

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def trySet(obj, value, note="Default"):
    try:
        obj.set(value)
    except:
        log.error(f"Can't set data (%s)" % (note))

def trySetBool(obj, value, note="Default"):
    if value is None:
        log.erorr(f"Can't set data (%s)" % (note))
        return
    trySet(obj, 1 if value else 0, note)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='IP', required=True)
    parser.add_argument('--token', help='token', required=True)
    parser.add_argument('--port', help='prometheus port', required=True)
    parser.add_argument('--model', help='miot model, use for unsupported.')
    args = parser.parse_args()

    airpurifier = airpurifier_miot.AirPurifierMiot(args.ip, args.token, model=args.model)

    temperature = Gauge('airpurifier_temp', 'temp, C')
    humidity = Gauge('airpurifier_humidity', 'humidity')
    aqi = Gauge('airpurifier_aqi', 'aqi')
    power = Gauge('airpurifier_power', 'power state')
    fan_speed = Gauge('airpurifier_fan_speed', 'fan speed')
    filter_life_remaining = Gauge('airpurifier_filter_remaining', 'filter remaining %')
    filter_left_time = Gauge('airpurifier_filter_left_time', 'filter left day(s)')
    filter_hours_used = Gauge('airpurifier_filter_hours_used', 'filter used hour(s)')

    # start the server
    prometheus_client.start_http_server(int(args.port))
    log.info("Server started at port {}".format(args.port))

    # update metrics every 5 sec
    while True:
        try:
            status = airpurifier.status()
            log.debug(status)
        except:
            log.error("Can't get information from device")
            continue
        #if (status.temperature is None):
        #    log.error("Can't get data from device")
        #    continue

        trySet(temperature, status.temperature, "temperature:")
        trySet(humidity, status.humidity, "humidity")
        trySet(aqi, status.aqi, "aqi")
        trySet(fan_speed, status.motor_speed, "moter_speed")
        trySet(filter_life_remaining, status.filter_life_remaining, "filter_remaining")
        trySet(filter_left_time, status.filter_left_time, "filter_left_time")
        trySet(filter_hours_used, status.filter_hours_used, "filter_hours_used")
        trySetBool(power, status.power, "power")

        time.sleep(5)


if __name__ == '__main__':
    main()