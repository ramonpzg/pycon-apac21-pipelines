
import json, os, pickle, sys, pandas as pd, numpy as np
import sklearn.metrics as metrics

model_file = sys.argv[1]
test_file = os.path.join(sys.argv[2], "test.csv")
scores_file = os.path.join('metrics', 'metrics.json')

with open(model_file, "rb") as fd:
    model = pickle.load(fd)

X_test = pd.read_csv(test_file)
y_test = X_test.pop('rented_bike_count')

predictions = model.predict(X_test.values)

mae = metrics.mean_absolute_error(y_test.values, predictions)
rmse = np.sqrt(metrics.mean_squared_error(y_test.values, predictions))
r2_score = model.score(X_test.values, y_test.values)

with open(scores_file, "w") as fd:
    json.dump({"MAE": mae, "RMSE": rmse, "R^2":r2_score}, fd, indent=4)
