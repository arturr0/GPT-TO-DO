from flask import Flask, request, jsonify
import your_ai_library

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = your_ai_library.predict(data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
