from flask import request,jsonify
from flask import Flask
from fastai.text import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
path = Path("")
learn = load_learner(path,"export.pkl")

@app.route('/api/threat_classification', methods=['POST'])
def get_text_prediction():
    json = request.get_json()
    #print("data")
    data = json["data"]
    a  = classify(data)
    return a

def classify(data):
        losses = learn.predict(data)
        return   '{"ans": "' + str(losses[0]) + '"}'

@app.route('/api/feedback',methods = ['POST'])
def put_feedback():
    #get_data("abc",0,0,0,0,0,0)
    json = request.get_json()
    data = json["data"]
    text = data["text"]
    flags = json["data"]["flag"]

    get_data(text,flags["toxic"],flags["severe_toxic"],flags["obscene"],flags["threat"],flags["insult"],flags["identity_hate"])
    return "True"

if __name__ == '__main__':
    app.run(debug=True)