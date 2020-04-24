FROM python:3.8.1-alpine3.11

ADD ./app/ /app/

WORKDIR /app/

RUN apk add --no-cache gcc libc-dev mariadb-dev linux-headers && \
    pip install --requirement requirements.txt && \
    wget --continue https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz --output-document geckodriver.tar.gz && \
    tar --extract --gzip --file geckodriver.tar.gz && \
    rm geckodriver.tar.gz

CMD ["uwsgi", \
     "--http-socket", "0.0.0.0:80", \
     "--wsgi", "run:app"]
