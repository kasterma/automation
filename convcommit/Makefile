.PHONY: venv
venv:
	python3.7 -m venv venv
	. venv/bin/activate ; pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv
	rm -rf convc.egg-info

.PHONY: test
test:
	pytest tests
