# build both dockers in the minikube
add-to-minikube: app-build-mk alembic-build-mk

k8s-app k8s-pg k8s-clean k8s-setup k8s-add-type: k8s-%:
	cd k8s ; ${MAKE} $*

app-build app-build-mk: app-%:
	cd app ; ${MAKE} $*

alembic-build alembic-build-mk: alembic-%:
	cd alembic ; ${MAKE} $*
