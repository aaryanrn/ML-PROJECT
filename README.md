# Hospital Readmission Prediction

## Overview
This project involves predicting hospital readmissions using a dataset containing patient demographic, diagnostic, and treatment-related information. The goal is to preprocess the data effectively and train machine learning models to predict whether a patient is likely to be readmitted.

## Dataset Description
The dataset contains the following key features:
- **race**: Categorical feature representing the patient's race.
- **gender**: Patient's gender.
- **age**: Patient's age group.
- **diag_1, diag_2, diag_3**: Primary and secondary diagnosis codes.
- **max_glu_serum**: Test result for maximum glucose serum.
- **A1Cresult**: Hemoglobin A1C test result.
- **readmitted**: Target variable indicating if the patient was readmitted.

## Steps Performed

### 1. Data Preprocessing
- **Handling Missing Values**:
  - Replaced missing values in columns like `diag_1`, `diag_2`, and `diag_3`.
  - Dropped rows where critical features like `race` or `gender` were invalid or missing.

- **Encoding Categorical Features**:
  - Used one-hot encoding for `race`.
  - Applied label encoding to features like `gender`.

- **Feature Transformation**:
  - Created `level1` and `level2` categories for diagnosis codes based on ICD classifications.
  - Converted `max_glu_serum` and `A1Cresult` into numeric features.

### 2. Exploratory Data Analysis (EDA)
- Performed descriptive statistics to understand the distribution of features.
- Visualized relationships between features and the target variable (`readmitted`).

### 3. Model Training
- Split the data into training and testing sets.
- Trained machine learning models such as Logistic Regression, Random Forest, and Gradient Boosting.
- Evaluated models using metrics like accuracy, precision, recall, and F1-score.

## Usage

### Prerequisites
- Python 3.8+
- Required libraries: pandas, numpy, scikit-learn, matplotlib, seaborn

### Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/your-username/hospital-readmission.git
cd hospital-readmission
pip install -r requirements.txt
```

### Running the Code
 To launch the app:
   ```bash
   python app.py or flask run
   ```

## Results
- Achieved an F1-score of X on the test set.
- Key insights from the analysis:
  - Diagnosis codes and age are significant predictors of readmission.
  - Certain race groups showed higher readmission rates, indicating potential disparities.

## Future Work
- Incorporate additional features like medication history or length of stay.
- Use advanced techniques like deep learning for better predictions.
- Explore fairness metrics to ensure equitable predictions across demographic groups.

## Contributing
Feel free to fork the repository and submit pull requests for improvements. All contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Contact
For any questions or suggestions, please contact:
- **Name**: Aaryan Agrawal
- **Email**: itsaaryanagrawal@gmail.com

