DOCKER_IMAGE=kasterma/devpi
DOCKER_TAG=0.0.0

build:
	docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .

# refresh requirements.txt from base-requirements.txt; only needed when desiring to test with possibly newer versions
freeze:
	cp base-requirements.txt requirements.txt
	${MAKE} build
	docker run -t ${DOCKER_IMAGE}:${DOCKER_TAG} pip freeze > requirements.txt

run:
	docker run ${DOCKER_IMAGE}:${DOCKER_TAG}