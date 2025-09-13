from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)

# Load model and encoders
try:
    model=pickle.load(open('LinearRegressionModel.pkl','rb'))
    with open('label_encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    car=pd.read_csv('Cleaned_Car_data.csv')
except FileNotFoundError:
    print("Model files not found. Please run train_model.py first.")
    model = None
    encoders = None
    car = None

@app.route('/',methods=['GET','POST'])
def index():
    if car is None:
        return "Model not loaded. Please run train_model.py first.", 500
    
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()

    companies.insert(0,'Select Company')
    return render_template('index.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    if model is None or encoders is None:
        return "Model not loaded. Please run train_model.py first.", 500

    company=request.form.get('company')
    car_model=request.form.get('car_models')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    driven=request.form.get('kilo_driven')

    # Encode the input data
    try:
        company_encoded = encoders['company_encoder'].transform([company])[0]
        name_encoded = encoders['name_encoder'].transform([car_model])[0]
        fuel_type_encoded = encoders['fuel_type_encoder'].transform([fuel_type])[0]
        
        # Create input array
        input_data = np.array([name_encoded, company_encoded, int(year), int(driven), fuel_type_encoded]).reshape(1, 5)
        
        prediction = model.predict(input_data)
        print(f"Prediction: {prediction[0]}")
        
        return str(np.round(prediction[0],2))
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error in prediction. Please check your input.", 400



if __name__=='__main__':
    app.run()
    
    
