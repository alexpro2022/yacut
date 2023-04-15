FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY migrations/ ./migrations
COPY yacut/ ./yacut
ENV FLASK_APP yacut
CMD flask db upgrade && flask run --host=0.0.0.0

