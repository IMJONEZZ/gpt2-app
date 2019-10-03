from flask import Flask, request, jsonify
import generation


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = generation.main(model_type='gpt2', model_name_or_path='gpt2', prompt=str(data))
    return text


if __name__ == '__main__':
    app.run(port=3000, debug=True)