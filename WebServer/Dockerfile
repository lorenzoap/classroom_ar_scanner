FROM python:3.8.1-alpine3.11

ADD ./app/ /app/

WORKDIR /app/

RUN apk add --no-cache gcc libc-dev mariadb-dev && \
    pip install --requirement requirements.txt

CMD ["python", "run.py"]
