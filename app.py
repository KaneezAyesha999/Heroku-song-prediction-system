from flask import Flask, render_template, request
#import jsonify 
import requests 
import pickle
import numpy as np
import pandas as pd
import sklearn
app = Flask(__name__)
model = pickle.load(open('Logistic_Regression_Model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    Song_Id = request.form.get('Song_Id')
    Artist_Name = request.form.get('Artist_Name')
    Year = request.form.get('Year')
    if(Artist_Name=='Wiz Khalifa'):
        Artist_Name=0
    elif (Artist_Name=='Adele'):
        Artist_Name=1
    elif (Artist_Name=='OneRepublic'):
        Artist_Name=2
    elif (Artist_Name=='Katy Perry'):
        Artist_Name=3
    elif (Artist_Name=='Rihanna and Calvin Harris'):
        Artist_Name=4
    elif (Artist_Name=='Avicii'):
        Artist_Name=5
    elif (Artist_Name=='Rihanna'):
        Artist_Name=6
    elif (Artist_Name=='Lady Gaga'):
        Artist_Name=7
    elif (Artist_Name=='Lucy Dacus'):
        Artist_Name=8
    elif (Artist_Name=='Travis Barker'):
        Artist_Name=9

    #input_features = [float(x) for x in request.form.values()]
    #features_value = [np.array(input_features)]
    
    #features_name = [ 'Song_Id',  'Artist_Name', 'Year']
    #df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict([[ Song_Id, Artist_Name, Year ]])
    
    return render_template('index.html', prediction_text='Predicted Song Name{}'.format(output) )

if __name__=="__main__":
    app.run(debug=True)