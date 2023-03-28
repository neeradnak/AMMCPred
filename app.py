import streamlit as st
import pickle
import pandas as pd
from PIL import Image

st.set_page_config(page_title="AMMC Prediction   App",page_icon="t.png",layout="wide")
st.header("""AMMC Prediction""")
st.write('---')

# SIDEBAR
img1 = Image.open('t.png')
st.sidebar.image(img1)
st.sidebar.header("Specify Input Parameters")

x = pd.read_csv('filtered_data.csv')
x = x.iloc[:,:9]

def user_input_features():
    matrix = st.sidebar.selectbox('Matrix',("Al7075","Al6061"))
    matrix_p = st.sidebar.slider('Matrix Percent',float(x['Matrix %'].min()),float(x['Matrix %'].max()),float(x['Matrix %'].mean()))
    size1 = st.sidebar.slider('Size-1',float(x['Size1'].min()),float(x['Size1'].max()),float(x['Size1'].mean()))
    rnf1_p = st.sidebar.slider('RNF1 Percent',float(x['RNF1 %'].min()),float(x['RNF1 %'].max()),float(x['RNF1 %'].mean()))
    size2 = st.sidebar.slider('Size-2',float(x['Size2'].min()),float(x['Size2'].max()),float(x['Size2'].mean()))
    rnf2_p = st.sidebar.slider('RNF2 Percent', float(x['RNF2%'].min()), float(x['RNF2%'].max()), float(x['RNF2%'].mean()))
    stiring_time = st.sidebar.slider('Stiring Time', float(x['stiring time'].min()), float(x['stiring time'].max()), float(x['stiring time'].mean()))
    stir_speed_mixing = st.sidebar.slider('Stir Speed Mixing', float(x['stir speed mixing'].min()),float(x['stir speed mixing'].max()), float(x['stir speed mixing'].mean()))
    temperature = st.sidebar.slider('Temperature', float(x['temperature'].min()), float(x['temperature'].max()), float(x['temperature'].mean()))

    if matrix == "Al7075":
        matrix = 1
    else:
        matrix=2

    data = {'Matrix':matrix,
            'Matrix %':matrix_p,
            'Size1':size1,
            'RNF1 %':rnf1_p,
            'Size2':size2,
            'RNF2%':rnf2_p,
            'stiring time (min)':stiring_time,
            'stir speed mixing(RPM)':stir_speed_mixing,
            'temperature':temperature}

    df = pd.DataFrame(data,index=[0])
    return df

df = user_input_features()

st.header('Specified Input Parameters')
st.write(df)
st.write('---')

b1 = st.sidebar.button('Predict Tensile Strength')
b2 = st.sidebar.button('Predict BHN')

if b1:
    model = pickle.load(open('model_TS.pkl', 'rb'))
    prediction = model.predict(df)
    st.header("Prediction of Tensile Strength")
    st.write(prediction)
    st.write('---')
if b2:
    model = pickle.load(open('model_BHN.pkl', 'rb'))
    prediction = model.predict(df)
    st.header("Prediction of BHN")
    st.write(prediction)
    st.write('---')

