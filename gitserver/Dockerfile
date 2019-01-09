FROM alpine:latest
LABEL maintainer "Bart Kastermans <kasterma@kasterma.net>"

ENV HOME /home/git
ENV AUTH_KEYS=${HOME}/.ssh/authorized_keys

RUN apk --no-cache add bash git openssh
RUN ssh-keygen -A   # generate host keys
RUN adduser -D -h ${HOME} -s /usr/bin/git-shell git && passwd -u git
RUN mkdir -p ${HOME}/.ssh
RUN touch ${AUTH_KEYS} && chown git:git ${AUTH_KEYS} && chmod 600 ${AUTH_KEYS}
RUN mkdir -p ${HOME}/git-shell-commands/
COPY no-interactive-login ${HOME}/git-shell-commands/
COPY create_repo /usr/bin/create_repo

EXPOSE 22
WORKDIR ${HOME}

COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["arg1", "arg2", "arg3"]
