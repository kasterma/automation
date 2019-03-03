.PHONY: setup generate monitor

setup:
	python app.py setup

generate:
	python app.py generate

monitor:
	python app.py monitor

build:
	docker build -t schema_app:0.0.0 .

build-mk:
	eval $(minikube docker-env) ; docker build -t schema_app:0.0.0 .
