from flask import Flask, request
import pandas as pd 
import numpy as np 
import pickle 
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('bna_rfc.pkl', 'rb')
rfc = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Bank Note Authentication"

@app.route('/predict', methods=["GET"])
def predict_note_auth():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    model_input = np.array([[variance, skewness, curtosis, entropy]])
    prediction = rfc.predict(model_input)
    return "The predicted value is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=rfc.predict(df_test)
    
    return str(list(prediction))

    

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
