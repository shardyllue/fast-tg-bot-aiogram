FROM python:3.11

WORKDIR /app

COPY . .

RUN pip3 install --upgrade setuptools

RUN poetry install

RUN chmod 755 .