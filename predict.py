
import pickle
from flask import Flask
from flask import request
from flask import jsonify


# Load the model

input_file = 'final_model.bin'


# Load the model from the pickle file
with open(input_file, 'rb') as f_in: 
    dv, pca, model = pickle.load(f_in)


app = Flask('delay')

@app.route('/predict', methods=['POST'])
def predict():
    flight = request.get_json()
    # Delete id and numberflight from the request
    if 'id' in flight:
        del flight['id']
    if 'flight' in flight:
        del flight['flight']

    X = dv.transform([flight])
    X = pca.transform(X)
    y_pred = model.predict_proba(X)[0, 1]
    delay = y_pred >= 0.5
    result = {
        'delay_probability': float(y_pred),
        'delay': bool(delay)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0',port=9696)


