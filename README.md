# Dockerized Django App

In this repo I created dockerized web application based on this book:
Django for Professionals, William S. Vincent

## some implementation details
dockerization by creating Dockerfile and **docker-compose.yml** is done.
we costomised user model to contains email and username by extending **AbstractModel**
django connected to **postgresql**.
Also some test cases is written for testing functionalities.

## usage
after cloning this repo and installing docker, for running in background at root directory (i.e. near manage.py):
`docker build . ` , `docker compose up -d --build`
