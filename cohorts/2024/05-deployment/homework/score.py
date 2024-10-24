import pickle 


# unpickling the dv and model
with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)

with open('model1.bin', 'rb') as model_file:
    model = pickle.load(model_file)

client = {"job": "management", "duration": 400, "poutcome": "success"}

# in order to score the client I need to 
X_val = dv.transform(client)
y_pred  =  model.predict_proba(X_val)[:, 1]

print(y_pred)

