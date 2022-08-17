FROM python:3.8
RUN	apt update
RUN	apt install -y vim

WORKDIR /usr/src/app

RUN	pip install --upgrade pip
RUN	pip install pipenv 

copy . .

RUN	pipenv install
RUN	pipenv install flask py-ms[all]
