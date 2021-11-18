
import os, pickle, sys, pandas as pd
from xgboost import XGBRFRegressor

input_data = sys.argv[1]
output = os.path.join('models', 'rf_model.pkl')
seed, n_est = 42, 100

X_train = pd.read_csv(input_data)
y_train = X_train.pop('rented_bike_count')

rf = XGBRFRegressor(n_estimators=n_est, seed=seed)
rf.fit(X_train.values, y_train.values)

with open(output, "wb") as fd: pickle.dump(rf, fd)
