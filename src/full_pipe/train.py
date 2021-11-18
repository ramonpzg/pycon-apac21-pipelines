
import os, pickle, sys, pandas as pd
<<<<<<< HEAD
from catboost import CatBoostRegressor
=======
from lightgbm import LGBMRegressor
>>>>>>> a1ecba27c1cfae510ef08a9a83ffd42ec7544b0b

input_data = sys.argv[1]
output = os.path.join('models', 'rf_model.pkl')
seed, n_est = 42, 100

X_train = pd.read_csv(input_data)
y_train = X_train.pop('rented_bike_count')

<<<<<<< HEAD
rf = CatBoostRegressor(n_estimators=n_est, random_state=seed)
=======
rf = LGBMRegressor(n_estimators=n_est, random_state=seed)
>>>>>>> a1ecba27c1cfae510ef08a9a83ffd42ec7544b0b
rf.fit(X_train.values, y_train.values)

with open(output, "wb") as fd: pickle.dump(rf, fd)
