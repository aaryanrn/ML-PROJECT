import json
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained ML model
model = joblib.load("final_model.joblib")

# Load the mappings from a JSON file
def load_mappings():
    with open('mappings.json', 'r') as file:
        mappings = json.load(file)
    return mappings

# Load all mappings
mappings = load_mappings()
gender_mapping = mappings['gender_mapping']
insulin_mapping = mappings['insulin_mapping']
race_mapping = mappings['race_mapping']
level1_diag_1_mapping = mappings['level1_diag_1']

# Default values for detailed features
DEFAULT_FEATURES = {
    "race": 2,
    "gender": 0,
    "age": 50,
    "admission_type_id": 1,
    "discharge_disposition_id": 1,
    "admission_source_id": 7,
    "time_in_hospital": 3,
    "num_lab_procedures": 1,
    "num_procedures": 0,
    "num_medications": 15,
    "number_diagnoses": 9,
    "metformin": 0,
    "repaglinide": 0,
    "nateglinide": 0,
    "chlorpropamide": 0,
    "glimepiride": 0,
    "acetohexamide": 0,
    "glipizide": 0,
    "glyburide": 0,
    "tolbutamide": 0,
    "pioglitazone": 0,
    "rosiglitazone": 0,
    "acarbose": 0,
    "miglitol": 0,
    "troglitazone": 0,
    "tolazamide": 0,
    "insulin": 1,
    "glyburide-metformin": 0,
    "glipizide-metformin": 0,
    "glimepiride-pioglitazone": 0,
    "metformin-rosiglitazone": 0,
    "metformin-pioglitazone": 0,
    "change": 0,
    "diabetesMed": 1,
    "service_utilization": 0,
    "numchange": 0,
    "level1_diag_1": 1
}

# Important features for general input
IMPORTANT_FEATURES = [
    "gender", "age", "time_in_hospital", "num_lab_procedures", "num_medications",
    "number_diagnoses", "insulin", "diabetesMed", "change"
]

@app.route('/')
def front():
    return render_template('front.html')

@app.route('/prediction')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form
    mode = user_input.get("mode")

    try:
        if mode == "detailed":
            # Gather all feature inputs from the user
            features = {}
            for key in DEFAULT_FEATURES.keys():
                value = user_input.get(key, None)
                if value is None:
                    features[key] = DEFAULT_FEATURES[key]
                else:
                    # Map categorical fields
                    if key == "gender":
                        features[key] = gender_mapping.get(value.lower(), DEFAULT_FEATURES[key])
                    elif key == "insulin":
                        features[key] = insulin_mapping.get(value.lower(), DEFAULT_FEATURES[key])
                    elif key == "race":
                        features[key] = race_mapping.get(value, DEFAULT_FEATURES[key])
                    elif key == "level1_diag_1":
                        features[key] = level1_diag_1_mapping.get(value, DEFAULT_FEATURES[key])
                    else:
                        features[key] = float(value)
        else:  # General mode
            # Gather only important features
            features = {}
            for key in IMPORTANT_FEATURES:
                value = user_input.get(key, None)
                if value is None:
                    features[key] = DEFAULT_FEATURES[key]
                else:
                    if key == "gender":
                        features[key] = gender_mapping.get(value.lower(), DEFAULT_FEATURES[key])
                    elif key == "insulin":
                        features[key] = insulin_mapping.get(value.lower(), DEFAULT_FEATURES[key])
                    else:
                        features[key] = float(value)
            # Fill in the rest with default values
            for key in DEFAULT_FEATURES.keys():
                if key not in features:
                    features[key] = DEFAULT_FEATURES[key]

        # Convert features to the input format required by the model
        feature_values = [features[key] for key in DEFAULT_FEATURES.keys()]

        # Predict using the model
        prediction = model.predict([feature_values])
        result = "Yes" if prediction[0] == 1 else "No"

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)