FROM python:3.5.3

WORKDIR /app/

COPY requirements.txt /app/
COPY app.py __init__.py /app/

RUN pip install -r ./requirements.txt


# ENTRYPOINT /bin/bash

EXPOSE 5002

ENTRYPOINT python ./app.py

