# The Shop API

> Web API designed for online shopping. You may use the project as a boilerplate for your needs as well.

## Project Summary:
[Click me to see the summary](SUMMARY.md)

## Documentation:
[API Doc](SUMMARY.md)


# Tool Chain:
+ Base Framework: Flask
+ ORM: SqlAlchemy
+ Serializer: Marshmallow
+ Server: gunicorn
+ Load-Balancer: nginx
+ DB: Mysql
+ UnitTest: pytest

## Project Setup:
Run the whole project 
```
make run
```

Init DB
```
make init
```

Doing migration
```
make migrate
```

Upgrade to DB
```
make upgrade
```

Run tests
```
make test
```

List all routes
```
make routes
```

Run the project under docker mode
```
docker-compose up --build
```

Reference:
You may find everything amazing available online.

+ M$ Rest API guideline: https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#readme
+ SQL Alchemy doc: https://docs.sqlalchemy.org/en/13/orm/tutorial.html

