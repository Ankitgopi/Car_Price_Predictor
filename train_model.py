import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the data
df = pd.read_csv('Cleaned_Car_data.csv')

# Create label encoders for categorical variables
le_company = LabelEncoder()
le_name = LabelEncoder()
le_fuel_type = LabelEncoder()

# Encode categorical variables
df['company_encoded'] = le_company.fit_transform(df['company'])
df['name_encoded'] = le_name.fit_transform(df['name'])
df['fuel_type_encoded'] = le_fuel_type.fit_transform(df['fuel_type'])

# Prepare features and target
X = df[['name_encoded', 'company_encoded', 'year', 'kms_driven', 'fuel_type_encoded']]
y = df['Price']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model and encoders
with open('LinearRegressionModel.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('label_encoders.pkl', 'wb') as f:
    pickle.dump({
        'company_encoder': le_company,
        'name_encoder': le_name,
        'fuel_type_encoder': le_fuel_type
    }, f)

print("Model trained and saved successfully!")
print(f"Model R² score: {model.score(X, y):.4f}")
