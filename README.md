# Flask APIs for Long-Running Tasks using Celery

_created by Austin Poor_


## About

This is a quick proof of concept for creating a [Flask](https://flask.palletsprojects.com) web API as a front-end for long-running tasks -- like making ML model predictions.

It uses the distributed task queue, [Celery](https://docs.celeryproject.org), to pass heavy processing off to worker nodes while freeing up the Flask server for handling requests.

When a user makes a request, the API diverts the processing to a Celery worker and responds with a location where the result will be stored when the processing is complete.

For example:

...


## Instructions for Use

1. Install the required packages in [requirements.txt](./requirements.txt), if necessary.
2. Run [build-model.py](./build-model.py) to train a `scikit-learn` logistic regression model on the iris dataset and then save it to the `models/` directory.
3. Start up Redis on port `6379`
4. Start up Celery with the command: `$ celery -A tasks worker`
5. Run [app.py](./app.py) to start up the `Flask` server

Then, the API will be up and running at: [http://localhost:5000/](http://localhost:5000/help)

You can test the server by running [test-api.py](./test-api.py).


## References

1. https://blog.miguelgrinberg.com/post/using-celery-with-flask
2. https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
3. https://docs.celeryproject.org/en/latest/userguide/tasks.html#instantiation


