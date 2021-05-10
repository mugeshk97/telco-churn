from flask import Flask, request, jsonify
import numpy as np
from src.utils import load_model, load_config


app = Flask(__name__)
model = load_model('model/model.pkl')
scaler = load_model('scaler/scaler.pkl')
config = load_config()
threshold = config['hyp']['threshold']

def get_label(pred, threshold):
    if pred[0] < threshold:
        y_hat = 1
    else:
        y_hat = 0
    return y_hat


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        df = request.get_json()
        inp = list(df.values())
        inp_array = np.array(inp, dtype = 'int64')
        inp_array = inp_array.reshape(1,-1)
        ip = scaler.transform(inp_array)
        pred = model.predict(ip)
        pred = get_label(pred, threshold= threshold)
        result = {'prediction': str(pred)}
    return jsonify(result)

if __name__ == '__main__':
	app.run(debug=True)