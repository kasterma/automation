DOCKER_IMAGE=kasterma/devpi
DOCKER_TAG=0.0.0

build:
	docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .

# refresh requirements.txt from base-requirements.txt; only needed when desiring to test with possibly newer versions
freeze:
	cp base-requirements.txt requirements.txt
	${MAKE} build
	docker run -t --entrypoint "" ${DOCKER_IMAGE}:${DOCKER_TAG} pip freeze > requirements.txt

run:
	docker run --rm -p 8989:8080 ${DOCKER_IMAGE}:${DOCKER_TAG}

run-bash:
	docker run --rm -ti --entrypoint bash ${DOCKER_IMAGE}:${DOCKER_TAG}
