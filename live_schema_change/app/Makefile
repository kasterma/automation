DOCKER_TAG=0.0.2

.PHONY: setup generate monitor

setup:
	python app.py setup

generate:
	python app.py generate

monitor:
	python app.py monitor

build:
	docker build -t schema_app:${DOCKER_TAG} .

build-mk:
	eval $$(minikube docker-env) ; docker build -t schema_app:${DOCKER_TAG} .
