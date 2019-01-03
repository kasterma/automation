DOCKER_IMAGE=kasterma/devpi
DOCKER_TAG=$(shell cat VERSION)

.PHONY: build
build:
	docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .

# refresh requirements.txt from base-requirements.txt; only needed when desiring to test with possibly newer versions
.PHONY: freeze
freeze:
	cp base-requirements.txt requirements.txt
	${MAKE} build
	docker run -t --entrypoint "" ${DOCKER_IMAGE}:${DOCKER_TAG} pip freeze > requirements.txt

.PHONY: run
run:
	docker run --rm -p 8989:8080 --name devpi ${DOCKER_IMAGE}:${DOCKER_TAG}


.PHONY: run-bash
run-bash:
	docker run --rm -ti --entrypoint bash ${DOCKER_IMAGE}:${DOCKER_TAG}
