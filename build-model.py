
import pickle
from pathlib import Path
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Create models directory if necessary
Path("models").mkdir(exist_ok=True)
MODEL_PATH = "./models/lm-iris.pkl"

# Load the data
iris = load_iris()
X, y = iris["data"], iris["target"]

# Train the model
lm = LogisticRegression(
    max_iter=100_000
).fit(
    X, y
)

# Print results
print("Model trained.")
print(f"Model score: {lm.score(X,y):.4f}")
print(f"Pickling model to: {MODEL_PATH}")

# Save the pickled model
with open(MODEL_PATH,"wb") as f:
    pickle.dump(lm,f)
