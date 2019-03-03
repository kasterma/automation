app:
	kubectl apply --record -f app.yaml

pg:
	kubectl apply --record -f postgres.yaml

clean:
	kubectl delete -f app.yaml
	kubectl delete -f postgres.yaml
