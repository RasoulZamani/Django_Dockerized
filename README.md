# Dockerized Django App

In this repo I created dockerized web application based on this book:
Django for Professionals, William S. Vincent

## some implementation details
this app has basic functionality like: **login, logout** and **signup**.

**bootstrap5** and **crispy_forms** is used to better style

dockerization by creating Dockerfile and **docker-compose.yml** is done.

we costomised user model to contains email and username by extending **AbstractModel**
django connected to **postgresql**.

Also some **test** cases is written for testing functionalities.

for more speed, it is better to collect all static files by `python manage collectstatic`. setting for this command are:
```
STATIC_ROOT         = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
```

athentication is done by third party app named: **django-allath**, so we can login based on email instead of username. for now, signup email is send to console and can be seen by `docker compose logs`.

____________________________________________________________________________________
## usage
after cloning this repo and installing docker, for running in background at root directory (i.e. near manage.py):  `docker compose up -d --build`

for test run:
`docker compose exec web python manage.py test`
(web in this command is the service name here)
