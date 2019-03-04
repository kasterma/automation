DOCKER_TAG=0.0.0

build:
	docker build -t schema_alembic:${DOCKER_TAG} .

build-mk:
	eval $$(minikube docker-env) ; docker build -t schema_alembic:${DOCKER_TAG} .
