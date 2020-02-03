# The Shop API

> Web API designed for online shopping.

## Project Summary:
[Click me to see the summary](SUMMARY.md)

# Tool Chain:
+ Base Framework: Flask
+ ORM: SqlAlchemy
+ Serializer: Marshmallow
+ Server: gunicorn
+ Load-Balancer: nginx
+ DB: Mysql
+ Seed: Flask-Seeder
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

Run the project under docker mode
```
docker-compose up --build
```

## References:

