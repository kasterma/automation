docker_tag=airflow
docker_version=0.0.0

.PHONY: build
build:
	docker build -t ${docker_tag}:${docker_version} .

.PHONY: run
run:
	docker run -p 8080:8080 ${docker_tag}:${docker_version}
