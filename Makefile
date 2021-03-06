run:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run flask run
test:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run pytest
init:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run flask db init
migrate:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run flask db migrate
upgrade:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run flask db upgrade
seed:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run flask seed
routes:
	export FLASK_DEBUG=True FLASK_APP=shop/app.py && pipenv run flask routes

.PHONY: run test init migrate upgrade seed routes
