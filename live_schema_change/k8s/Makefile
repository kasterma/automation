app:
	kubectl apply --record -f app.yaml

setup:
	kubectl apply --record -f dbsetup.yaml

pg:
	kubectl apply --record -f pg_service.yaml
	kubectl apply --record -f postgres.yaml

clean:
	kubectl delete -f app.yaml
	kubectl delete -f postgres.yaml pg_service.yaml
