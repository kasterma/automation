# build both dockers in the minikube
.PHONY: add-to-minikube
add-to-minikube: app-build-mk alembic-build-mk

.PHONY: k8s-generate k8s-monitor k8s-pg k8s-clean k8s-setup k8s-add-type
k8s-generate k8s-monitor k8s-pg k8s-clean k8s-setup k8s-add-type: k8s-%:
	cd k8s ; ${MAKE} $*

.PHONY: app-build app-build-mk
app-build app-build-mk: app-%:
	cd app ; ${MAKE} $*

.PHONY: alembic-build alembic-build-mk
alembic-build alembic-build-mk: alembic-%:
	cd alembic ; ${MAKE} $*
