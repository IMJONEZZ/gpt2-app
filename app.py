from flask import Flask, request, jsonify, render_template
import os
import generation


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    assert request.method == 'POST'
    words = request.form['text']
    number = int(request.form['number'])
    text = generation.main(model_type='gpt2', 
                        model_name_or_path='gpt2', 
                        prompt=str(words), 
                        length=number)
    out = str(words) + ' ' + str(text)
    return render_template('index.html', text=out)
    
if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000), debug=False)