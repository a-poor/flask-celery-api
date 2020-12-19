
import pickle
import numpy as np
from sklearn.datasets import load_iris

from flask import Flask, request

import tasks
from celery.result import AsyncResult

app = Flask(__name__)

@app.route("/help")
def get_help():
    iris = load_iris()
    feature_names = iris["feature_names"]
    target_names = iris["target_names"]

    features = "\n".join(f"<li>{f}</li>" for f in feature_names)
    targets = "\n".join(f"<li>{t}</li>" for t in target_names)
    return f"""
<h1>Iris Prediction API Help</h1>
<p></p>
<h3>Feature Names</h3>
<ol>{features}</ol>
<h3>Target Names</h3>
<ol>{targets}</ol>
"""

@app.route("/predict",methods=["POST"])
def predict():
    req_input = request.get_json()
    res = tasks.predict.delay(req_input["input-data"])
    return {"result-url":f"/result/{res.task_id}"}

@app.route("/result/<task_id>")
def get_results(task_id: str):
    res = AsyncResult(task_id,app=tasks.app)
    if res.state == "SUCCESS":
        return {"status":res.state,"predictions":res.get()}
    return {"status":res.state}

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
