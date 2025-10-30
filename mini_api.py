from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

model=open('classifier.pkl','rb')
model = pickle.load(model)
#home page
@app.route("/")
def hello_world():
    return {"Message":"Hello Welcome to loan prediction system!!!"}

@app.route("/panda")
def hello_panda():
    return "<p>Hello, Panda!</p>"

@app.route("/ping")
def hello_ping():
    return {"message":"Hello Pong"}

@app.route("/predict", methods=['POST'])
def prediction():

    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Yes":
        Married = 1
    else:
        Married = 0

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    result = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}