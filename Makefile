run:
	export FLASK_DEBUG=True FLASK_APP=api/app.py && pipenv run flask run
test:
	export FLASK_DEBUG=True FLASK_APP=api/app.py && pipenv run pytest

.PHONY: run test
