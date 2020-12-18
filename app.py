
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

def validate_input(req):
    if not isinstance(req,dict):
        return False
    if "input-data" not in req:
        return False
    input_data = req["input-data"]
    if not isinstance(input_data,list):
        return False
    if not isinstance(input_data[0],list):
        return False
    if not isinstance(input_data[0][0],(int,float)):
        return False
    if len(input_data[0])
    return True

@app.route("/predict",methods=["POST"])
def predict():
    req_input = request.get_json()
    validate_input(req_input)
    res = tasks.predict(req_input[""])
    return {"key":"value"}

@app.route("/result/<task_id>")
def get_results(task_id: str):
    res = AsyncResult(task_id,app=tasks.app)
    if res.state == "SUCCESS":
        return {"status":"success","result":res.get()}
    return {"status":"working"}



if __name__ == "__main__":
    app.run(debug=True, port=5000)
