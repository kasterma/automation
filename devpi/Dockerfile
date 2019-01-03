FROM python:3.7
MAINTAINER Bart Kastermans <kasterma@kasterma.net>

ENV DEVPI_USER=devpi
ENV DEVPI_USER_HOME=/home/devpi
ENV DEVPI_HOME=${DEVPI_USER_HOME}/data

RUN addgroup -gid 1000 ${DEVPI_USER}
RUN useradd --uid 1000 --gid 1000 --home ${DEVPI_USER_HOME} ${DEVPI_USER}
RUN mkdir -p ${DEVPI_HOME}

ADD requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

ADD config.yaml /
ADD entrypoint.sh /
EXPOSE 8080

RUN chown -R ${DEVPI_USER}:${DEVPI_USER} ${DEVPI_USER_HOME} /config.yaml /entrypoint.sh
USER ${DEVPI_USER}

ENTRYPOINT /entrypoint.sh
