FROM python:3.7-slim

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
ENV FLASK_APP yacut
CMD flask db upgrade && flask run --host=0.0.0.0
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]