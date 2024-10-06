import pickle
import requests
from flask import Flask, request, jsonify


app = Flask('score')


# url = "YOUR_URL"
# client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
# requests.post(url, json=client).json()

with open('dv.bin', 'rb') as dv_file, open('model1.bin', 'rb') as model_file:
    dv = pickle.load(dv_file)
    model = pickle.load(model_file)


def score_client(client, dv, model):

    client = dv.transform(client)
    pred = model.predict_proba(client)[:, 1]
    return pred[0]

@app.route("/predict", methods=['POST'])
def predict():
    client = request.get_json()

    pred = score_client(client, dv, model)
    loan_granted = "Granted" if pred >= 0.5 else "Denied"

    res = {'probability': pred,
           "loan_granted": loan_granted}

    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

