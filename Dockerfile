FROM python:3.11

WORKDIR /app

COPY . .

RUN pip3 install --upgrade setuptools

RUN pip3 install -r ./requirements.txt

RUN chmod 755 .