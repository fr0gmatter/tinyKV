# tinyKV

tinyKV is a simple Key/Value microservice

This tinyKV example maps key to url, and returns a http redirect. Thus becoming a URL shortener if used with a small domain name 

## Instructions

First clone the repo

### to install

```
cd tinyKV
pip install pipenv

# install the requirements
pipenv install
# start virtual environment
pipenv shell  

python main.py

```
access by browser at localhost:5000

### to use the docker container

```
make
make run
pipenv shell
python main.py
```

if you don't have make, run the commands from the Makefile

In this code the key is mapped to a url. What else could the key be mapped to?
