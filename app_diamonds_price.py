import xgboost as xgb
import streamlit as st
import sklearn
import pandas as pd

#load the regression model
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

#caching the model for faster loading
@st.cache

# define the prediction
def predict(carat, cut, color, clarity, depth, table, x, y, z):
    if cut == 'Fair':
        cut = 0
    elif cut == 'Good':
        cut = 1
    elif cut == 'Very Good':
        cut = 2
    elif cut == 'Premium':
        cut = 3
    elif cut == 'Ideal':
        cut = 4

    if color == 'J':
        color = 0
    if color == 'I':
        color = 1
    if color == 'H':
        color = 2
    if color == 'G':
        color = 3
    if color == 'F':
        color = 4
    if color == 'E':
        color = 5
    if color == 'D':
        color = 6

    if clarity == 'I1':
        clarity = 0
    if clarity == 'SI2':
        clarity = 1
    if clarity == 'SI1':
        clarity = 2
    if clarity == 'VS2':
        clarity = 3
    if clarity == 'VS1':
        clarity = 4
    if clarity == 'VVS2':
        clarity = 5
    if clarity == 'VVS1':
        clarity = 6
    if clarity == 'IF':
        clarity = 7

    prediction = model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    
    return prediction


st.title('Diamond Price Predictor')
st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the characteristics of the diamond:')
carat = st.number_input('Carat weight:', min_value = 0.1, max_value = 10.0, value = 1.0)
cut = st.selectbox('Cut rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Clarity rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
depth = st.number_input('Diamond Depth Percentage:', min_value = 0.1, max_value = 100.0, value = 1.0)
table = st.number_input('Diamond Table Percentage:', min_value = 0.1, max_value = 100.0, value = 1.0)
x = st.number_input('Diamond Lenght(x) in mm:', min_value = 0.1, max_value = 100.0, value = 1.0)
y = st.number_input('Diamond Lenght(y) in mm:', min_value = 0.1, max_value = 100.0, value = 1.0)
z = st.number_input('Diamond Lenght(z) in mm:', min_value = 0.1, max_value = 100.0, value = 1.0)

if st.button('Predict Price'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'The predicted price of the diamond is ${price[0]:.2f} USD')