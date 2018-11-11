.PHONY: build
build:
	docker build -t gitserver .

.PHONY: run
run:  # run the docker, but with rm flag for development
	-docker network create autom
	docker run -d --rm --hostname gitserver --name gitserver -p2222:22 -e "PUBKEY=$(shell cat rsatestkey.pub)" --net autom gitserver

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