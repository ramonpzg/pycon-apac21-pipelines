
import os, pickle, sys
import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor

input_data = sys.argv[1]
output = os.path.join('models', 'rf_model.pkl')
seed = 42
n_est = 100

X_train = pd.read_csv(input_data)
y_train = X_train.pop('rented_bike_count')

rf = RandomForestRegressor(n_estimators=n_est, random_state=seed)
rf.fit(X_train.values, y_train.values)

with open(output, "wb") as fd:
    pickle.dump(rf, fd)
