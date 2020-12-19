# Flask APIs for Long-Running Tasks using Celery

_created by Austin Poor_


## About

This is a quick proof of concept for creating a [Flask](https://flask.palletsprojects.com) web API as a front-end for long-running tasks -- like making ML model predictions.

It uses the distributed task queue, [Celery](https://docs.celeryproject.org), to pass heavy processing off to worker nodes while freeing up the Flask server for handling requests.

When a user makes a request, the API diverts the processing to a Celery worker and responds with a location where the result will be stored when the processing is complete.

For example:

...


## Repo Structure

...


## Instructions for Use

...


## References

1. https://blog.miguelgrinberg.com/post/using-celery-with-flask
2. https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
3. https://docs.celeryproject.org/en/latest/userguide/tasks.html#instantiation


