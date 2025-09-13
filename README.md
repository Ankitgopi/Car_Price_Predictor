# Car Price Predictor

A Flask-based web application that predicts car prices based on various features like company, model, year, fuel type, and kilometers driven.

## Features

- Interactive web interface for car price prediction
- Machine learning model trained on car data
- Responsive design with Bootstrap
- Real-time price prediction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have the `LinearRegressionModel.pkl` file in the root directory
2. Run the application:
```bash
python application.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
car-price-predictor/
├── application.py          # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LinearRegressionModel.pkl  # Trained ML model (not included)
├── Cleaned_Car_data.csv   # Dataset
├── static/
│   └── css/
│       └── style.css      # Custom styles
└── templates/
    └── index.html         # Main HTML template
```

## Requirements

- Python 3.7+
- Flask
- Pandas
- NumPy
- Scikit-learn
- Flask-CORS

## Note

The `LinearRegressionModel.pkl` file is not included in this repository. You'll need to train and save your own model using scikit-learn.