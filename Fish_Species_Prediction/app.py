from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('your_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(data['features'])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
