import pickle

# Load both the DictVectorizer and model in a single block
with open('dv.bin', 'rb') as dv_file, open('model1.bin', 'rb') as model_file:
    dv = pickle.load(dv_file)
    model = pickle.load(model_file)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

def score_client(client, dv, model):

    client = dv.transform(client)
    pred = model.predict_proba(client)[:, 1]
    return pred[0]

if __name__ == "__main__":
    score = score_client(client, dv, model)
    print(f"The probablility the client is granted a loan is {score:.3f}")