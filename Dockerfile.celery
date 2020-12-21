FROM python:3.7
WORKDIR /app

RUN mkdir /app/models

COPY requirements.txt /app
COPY tasks.py /app
COPY models/lm-iris.pkl /app/models

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD celery -A tasks worker
