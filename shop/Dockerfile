FROM python:3.7-alpine

RUN mkdir /shop

COPY . /shop
WORKDIR /shop

RUN apk update \
  # bcrypt dependencies
  && apk add --virtual build-deps libffi-dev g++ python3-dev py-gunicorn

RUN pip install -r requirements.txt

ENV FLASK_APP /shop/app.py
ENV PYTHONPATH /

USER root
EXPOSE 5000

RUN ["chmod", "777", "start.sh"]

# Use api:create_app if you structure the app in factory pattern
ENTRYPOINT ["./start.sh"]
