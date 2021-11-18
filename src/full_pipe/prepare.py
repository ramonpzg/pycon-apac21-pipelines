
import pandas as pd
import os, sys

split = 0.30

raw_data_path = sys.argv[1]
train_path = os.path.join('data', '03_part', 'processed', 'train.csv')
test_path = os.path.join('data', '03_part', 'processed', 'test.csv')

# read the data
data = pd.read_csv(raw_data_path, encoding='iso-8859-1')

# add date vars
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(['Date', 'Hour'], inplace=True)
data["Year"] = data['Date'].dt.year
data["Month"] = data['Date'].dt.month
data["Week"] = data['Date'].dt.isocalendar().week
data["Day"] = data['Date'].dt.day
data["Dayofweek"] = data['Date'].dt.dayofweek
data["Dayofyear"] = data['Date'].dt.dayofyear
data["Is_month_end"] = data['Date'].dt.is_month_end
data["Is_month_start"] = data['Date'].dt.is_month_start
data["Is_quarter_end"] = data['Date'].dt.is_quarter_end
data["Is_quarter_start"] = data['Date'].dt.is_quarter_start
data["Is_year_end"] = data['Date'].dt.is_year_end
data["Is_year_start"] = data['Date'].dt.is_year_start
data.drop('Date', axis=1, inplace=True)

# add dummies
data = pd.get_dummies(data=data, columns=['Holiday', 'Seasons', 'Functioning Day'])

# Normalize columns
data.columns = ['rented_bike_count', 'hour', 'temperature', 'humidity', 'wind_speed', 'visibility', 
                'dew_point_temperature', 'solar_radiation', 'rainfall', 'snowfall', 'year', 
                'month', 'week', 'day', 'dayofweek', 'dayofyear', 'is_month_end', 'is_month_start',
                'is_quarter_end', 'is_quarter_start', 'is_year_end', 'is_year_start',
                'seasons_autumn', 'seasons_winter', 'seasons_summer', 'seasons_spring',
                'holiday_yes', 'holiday_no', 'functioning_day_no', 'functioning_day_yes']

n_train = int(len(data) - len(data) * split)
data[:n_train].reset_index(drop=True).to_csv(train_path, index=False)
data[n_train:].reset_index(drop=True).to_csv(test_path, index=False)
