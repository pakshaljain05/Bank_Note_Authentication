"""
Created on Fri May 21 2021
@author: pakshaljain
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("bna_rfc.pkl","rb")
rfc = pickle.load(pickle_in)


def predict_note_authentication(variance,skewness,curtosis,entropy):
   
    prediction = rfc.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

    

def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
   

if __name__=='__main__':
    main()