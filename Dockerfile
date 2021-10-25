FROM python:3.9-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/ayami-szk/PBL_test myapp

WORKDIR myapp

RUN pip install flask flask-sqlalchemy

ENV FLASK_APP test.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "11111"]
