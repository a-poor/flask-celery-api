
import pickle
import numpy as np
from celery import Celery

MODEL_PATH = "./models/log_iris.pkl"

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def predict(input_data):
    d = np.array(input_data)
    with open(MODEL_PATH,"rb") as f:
        lm = pickle.load(f)
    res = lm.predict(d)
    return res.tolist()
