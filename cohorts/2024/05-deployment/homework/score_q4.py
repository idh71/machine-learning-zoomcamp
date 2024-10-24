from flask import Flask, request, jsonify
import pickle
import requests

with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)

with open("model1.bin", 'rb') as model_file:
    model = pickle.load(model_file)


app = Flask('predict')

# client = {"job": "student", "duration": 280, "poutcome": "failure"}

def predict_score(client, dv, model):
    X_val = dv.transform(client)
    y_pred  =  model.predict_proba(X_val)[:, 1]

    return y_pred[0]


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    prediction = predict_score(client, dv, model)

    approved = True if prediction >= 0.5 else False

    result = {
    'score': float(prediction), ## we need to cast numpy float type to python native float type
    'approved': bool(approved),  ## same as the line above, casting the value using bool method
}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

