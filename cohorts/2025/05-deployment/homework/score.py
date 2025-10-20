import pickle


model_file = "model.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


# print(dv)
# print(model)

client = {"job": "management", "duration": 400, "poutcome": "success"}

X_val = dv.transform(client)

prediction = model.predict_proba(X_val)[0, 1]

print(f"the probability that the client with get a subsription is {prediction:.3f}")