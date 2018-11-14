FROM ubuntu:18.04

ENV AIRFLOW_VERSION=1.10.0
ENV AIRFLOW_USER=airflow
ENV AIRFLOW_USER_HOME=/home/airflow
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}/airflow
ENV AIRFLOW_GPL_UNIDECODE=yes

RUN addgroup -gid 1000 ${AIRFLOW_USER}
RUN useradd --uid 1000 --gid 1000 --home ${AIRFLOW_USER_HOME} ${AIRFLOW_USER}

RUN apt-get update
RUN apt-get -y install python3-pip

RUN pip3 install apache-airflow==${AIRFLOW_VERSION}
RUN airflow initdb

EXPOSE 8080

ADD entrypoint.sh /
ENTRYPOINT /entrypoint.sh
