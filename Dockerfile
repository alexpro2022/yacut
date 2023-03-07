FROM python:3.7-slim

WORKDIR /app
COPY migrations/ ./migrations
COPY yacut/ ./yacut
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
ENV FLASK_APP yacut
CMD flask db upgrade && flask run --host=0.0.0.0

