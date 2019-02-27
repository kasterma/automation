run:
	-docker network create autom
	docker run --rm --name jenkins --net autom -d -v jenkins_home:/var/jenkins_home -v /Users/kasterma/tmp/gittest/AAA:/AAA -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
