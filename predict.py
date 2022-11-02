import pickle
from flask import (
    Flask,
    request,
    jsonify
)

app = Flask(__name__)

with open('hotel_v.1.bin', 'rb') as f:
    dv, model= pickle.load(f)
    

def score_hotel(hotel):
    X = dv.transform([hotel])
    return model.predict_proba(X)[0, 1]

@app.route('/', methods=['GET'])
def home():
    return "<h1>API IS WORKING...</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    hotel = request.get_json()
    y_pred = score_hotel(hotel)
    is_cancelled = y_pred >= .5
    return jsonify(
        {
            'probability': float(y_pred.round(3)),
            'is_cancelled': bool(is_cancelled)
        }
    )

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)