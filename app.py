from flask import Flask, render_template
import pandas as pd

dataset = pd.read_csv('Car Price Predictor\clean_data.csv')


app = Flask(__name__)

@app.route('/')
def index():
    companies = sorted(dataset['company'].unique())
    car_models = sorted(dataset['name'].unique())
    years = sorted(dataset['year'].unique(), reverse=True)
    fuel_types = sorted(dataset['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models, years = years, fuel_types=fuel_types)

if __name__=='__main__':
    app.run(debug=True)