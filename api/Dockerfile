FROM python:3.7-alpine

COPY . /api
WORKDIR /api

RUN pip install -r requirements.txt
RUN pip install gunicorn

ENV FLASK_APP app.py

USER root
EXPOSE 5000

CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
