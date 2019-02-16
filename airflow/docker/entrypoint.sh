#!/usr/bin/env sh

# start the scheduler
airflow scheduler &

# start the web server, default port is 8080
airflow webserver -p 8080

while true; do
  echo hi
  sleep 10
done

