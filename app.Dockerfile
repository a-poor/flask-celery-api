FROM python:3.7
WORKDIR /app

COPY app.py /app
COPY tasks.py /app
COPY requirements.txt /app

EXPOSE 5000

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD [ "python", "app.py" ]
