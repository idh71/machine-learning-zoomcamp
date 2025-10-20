
import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
# customer = {
#     "gender": "female",
#     "seniorcitizen": 0,
#     "partner": "yes",
#     "dependents": "no",
#     "phoneservice": "no",
#     "multiplelines": "no_phone_service",
#     "internetservice": "dsl",
#     "onlinesecurity": "no",
#     "onlinebackup": "yes",
#     "deviceprotection": "no",
#     "techsupport": "no",
#     "streamingtv": "no",
#     "streamingmovies": "no",
#     "contract": "month-to-month",
#     "paperlessbilling": "yes",
#     "paymentmethod": "electronic_check",
#     "tenure": 24,
#     "monthlycharges": 29.85,
#     "totalcharges": (24 * 29.85)
# }

# client = {"job": "student", "duration": 280, "poutcome": "failure"}
# the client for Question 6
client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()



# response = requests.post(url, json=customer).json()
print(response)

if response['subsribe'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)