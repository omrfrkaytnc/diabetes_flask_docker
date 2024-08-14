from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class DiabetesForm(FlaskForm):
    Pregnancies = StringField("Pregnancies")
    Glucose = StringField("Glucose")
    BloodPressure = StringField("Blood Pressure")
    SkinThickness = StringField("Skin Thickness")
    Insulin = StringField("Insulin")
    BMI = StringField("BMI")
    DiabetesPedigreeFunction = StringField("Diabetes Pedigree Function")
    Age = StringField("Age")

    submit = SubmitField("Predict")