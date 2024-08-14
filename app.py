from flask import Flask, request, jsonify, session, url_for, redirect, render_template
import joblib
from helpers import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from diabetes_form import DiabetesForm


app = Flask(__name__)

# Modeli yükle
voting_clf_loaded = joblib.load("voting_clf.pkl")
scaler_loaded = joblib.load("scaler.pkl")


@app.route('/predict', methods=['POST'])

def make_prediction(model, scaler, sample_json):
    # parse input from request
    Pregnancies = sample_json['Pregnancies']
    Glucose = sample_json['Glucose']
    BloodPressure = sample_json['BloodPressure']
    SkinThickness = sample_json['SkinThickness']
    Insulin = sample_json['Insulin']
    BMI = sample_json['BMI']
    DiabetesPedigreeFunction = sample_json['DiabetesPedigreeFunction']
    Age = sample_json['Age']

    # Make an input vector
    values = pd.DataFrame(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]],
        columns=[
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
        ])



    X = diabetes_data_last_prep(values, scaler)

    # Predict
    prediction_real = model.predict(X)

    return prediction_real[0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/", methods=['GET','POST'])

def index():
    form = DiabetesForm()

    if form.validate_on_submit():
        session['Pregnancies'] = form.Pregnancies.data
        session['Glucose'] = form.Glucose.data
        session['BloodPressure'] = form.BloodPressure.data
        session['SkinThickness'] = form.SkinThickness.data
        session['Insulin'] = form.Insulin.data
        session['BMI'] = form.BMI.data
        session['DiabetesPedigreeFunction'] = form.DiabetesPedigreeFunction.data
        session['Age'] = form.Age.data

        return redirect(url_for("prediction"))
    return render_template("home.html", form=form)

voting_clf_loaded = joblib.load("voting_clf.pkl")


@app.route('/prediction')
def prediction():
    content = {'Pregnancies': int(session['Pregnancies']), 'Glucose': int(session['Glucose']),
               'BloodPressure': int(session['BloodPressure']), 'SkinThickness': int(session['SkinThickness']),
               'Insulin': int(session['Insulin']), 'BMI': float(session['BMI']),
               'DiabetesPedigreeFunction': float(session['DiabetesPedigreeFunction']), 'Age': int(session['Age'])}


    results = make_prediction(voting_clf_loaded, scaler_loaded, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
