FROM python:3.9-slim

RUN mkdir /app

COPY . /app/

WORKDIR /app

RUN apt update && apt install -y make

RUN make install

EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]





