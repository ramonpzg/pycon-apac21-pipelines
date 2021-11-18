
import sys, pandas as pd, numpy as np, streamlit as st
import statsmodels.api as sm
import statsmodels.formula.api as smf
from variables import *
from features import *
from statsmodels.graphics.regressionplots import plot_partregress_grid
import matplotlib.pyplot as plt
from pathlib import Path

data_input = sys.argv[1]
path = Path.cwd()

## data
df = pd.read_parquet(path.joinpath('data', 'processed', 'airbnb', data_input))
df['property_type'] = df['property_type'].apply(simplify)
df['room_type'] = df['room_type'].str.lower().str.replace(' ', '_').str.replace('/', '_')
df['log_price'] = np.log(df['price'])
df = pd.get_dummies(df, columns=['room_type', 'property_type'], prefix={'room_type':'rt', 'property_type': 'pt'})
X, y = sm.add_constant(df[independent]), df[dependent]

## normal model and summary
lr = sm.OLS(y.values, X.values).fit()
the_summary = lr.summary2(xname=list(X.columns))

## geospatial model and summary
f = fr'{dependent} ~ {" + ".join(independent)} + {neighbourhood}'
mod = smf.ols(f, data=df).fit()
the_geo_summary = mod.summary2()

## our app
st.title("Airbnb Statistical Modeling Report")
st.markdown(f"## This Analysis is for {df['city'].unique()[0]}")
st.sidebar.title("Normal vs Geospatial Analysis")
st.sidebar.markdown("Pick one of the 2")
st.sidebar.image("https://i.pinimg.com/originals/a3/cd/30/a3cd30c0ba0e7f827dfe22e7a7011cd8.gif")
side = st.sidebar.selectbox(
        'Pick Analysis', ["Normal Analysis", "Geospatial Analysis"], key='0')

if side == "Normal Analysis":
    st.markdown("### Non-Geospatial Report")
    st.text(the_summary)

    fig1 = plt.figure(figsize=(12, 10))
    plot_normal = plot_partregress_grid(lr, fig=fig1)
    
    st.markdown('#### Normal Charts')
    st.pyplot(plot_normal)
    
else:
    st.markdown("### Geospatial Report")
    st.text(the_geo_summary)
    
st.markdown("### Map")
st.map(df[geo_vars].sample(5000))
