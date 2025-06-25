from flask import Flask, request, render_template
import pandas as pd
import joblib  # used for loading the model

app = Flask(__name__)

# Use the full absolute path to your saved model
model_path = r"C:\Users\avant\Avantika Digicrome\Project 6\saved_models\rf_pipeline_2025-06-25-23-54-36.pkl"
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST']) # post work as a push in flask
def predict():
    try:
        feature_order = [
            'Store', 'Promo', 'SchoolHoliday', 'StoreType', 'Assortment',
            'CompetitionDistance', 'Promo2', 'Month', 'DayOfWeek', 'IsWeekend'
        ]

        input_values = [float(request.form.get(feature)) for feature in feature_order]
        input_df = pd.DataFrame([input_values], columns=feature_order)
        prediction = model.predict(input_df)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
