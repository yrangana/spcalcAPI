FROM python:3.9-slim

RUN mkdir /app

COPY . /app/

WORKDIR /app
# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y make --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN make install

EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]





