app:
	kubectl apply --record -f app.yaml

setup:
	kubectl apply --record -f dbsetup.yaml

add-type:
	kubectl apply --record -f db_migrate_add_type.yaml

pg:
	kubectl apply --record -f pg_service.yaml
	kubectl apply --record -f postgres.yaml

clean:
	kubectl delete -f app.yaml
	kubectl delete -f postgres.yaml pg_service.yaml
