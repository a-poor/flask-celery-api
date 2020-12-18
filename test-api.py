
import time
import requests
import numpy as np
from sklearn.datasets import load_iris
from urllib.parse import urljoin
from sklearn.metrics import accuracy_score

# Load the data (and select a subset)
iris = load_iris()
X, y = iris["data"], iris["target"]
n = 100
idxs = np.random.randint(0,len(X),n)
X, y = X[idxs], y[idxs]

# Make API request
base_url = "http://localhost:5000/"
resp = requests.post(
    urljoin(base_url,"/predict"),
    json={"input-data":X.tolist()}
)
result_url = urljoin(
    base_url,
    resp.json()["result-url"]
)

# Pause and wait for prediction to complete
time.sleep(1)

# Get predictions from API
resp = requests.get(result_url).json()
preds = np.array(resp["predictions"])
pred_acc = accuracy_score(y,preds)
print(f"Prediction accuracy: {pred_acc:.4f}")
