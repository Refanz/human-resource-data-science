import joblib
import pandas as pd

sample_data = pd.read_csv('data/employee_data.csv').sample(5)

model = joblib.load('model/model.joblib')
encoder = joblib.load('model/encoder.joblib')
scaler = joblib.load('model/scaler.joblib')
important_features = joblib.load('model/importance_features.joblib')
categorical_features = joblib.load('model/categorical_features.joblib')

def preprocessing(input_data):
    input_data = input_data.drop(columns=['EmployeeId', 'Attrition'])

    input_data[categorical_features] = encoder.transform(input_data[categorical_features])
    scaled = scaler.transform(input_data)
    processed_data = pd.DataFrame(scaled, columns=input_data.columns)

    return processed_data[important_features]

def predict_model(input_data):
    processed_data = preprocessing(input_data)
    prediction = model.predict(processed_data)
    return prediction

print("Prediction Result:")

result = predict_model(sample_data)
print(result)