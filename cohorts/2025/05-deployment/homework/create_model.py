import pandas as pd
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

output_file = f'model.bin'


df = pd.read_csv('bank-full.csv', sep=";")

# print(df.columns.tolist())

# print(df.head())

# print(df['y'].value_counts())


features = ['job', 'duration', 'poutcome']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)
df['y'] = df['y'].map({'yes': 1, 'no': 0})
y = df['y'].values

model = LogisticRegression(max_iter=1000).fit(X, y)

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

