DOCKER_IMAGE=kasterma/gitserver
DOCKER_TAG=0.0.0

.PHONY: build
build:
	docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .

.PHONY: run
run:  # run the docker, but with rm flag for development
	-docker network create autom
	docker run -d --rm --hostname gitserver --name gitserver -p2222:22 -e "PUBKEY=$(shell cat rsatestkey.pub)" \
		-v gitserver:/home/git/data --net autom ${DOCKER_IMAGE}:${DOCKER_TAG}

.PHONY: stop
stop:
	docker stop gitserver

.PHONY: test
test:
	shellcheck entrypoint.sh
	shellcheck create_local_repo.sh
	shellcheck no-interactive-login


.PHONY: genkeys
genkeys:
	ssh-keygen -f rsatestkey
