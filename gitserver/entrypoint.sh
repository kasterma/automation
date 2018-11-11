#!/usr/bin/env bash

echo "$0"
echo "$1"
echo "$2"
echo "$3"

echo "$PUBKEY" >> "${HOME}/.ssh/authorized_keys"

/usr/sbin/sshd -De &
# -D do not detach
# -e send output to stderr

pid="$!"
echo "pid=$pid"

ps ax

wait $pid