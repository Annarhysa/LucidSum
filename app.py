from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

def input_data():
    df = pd.read_csv('data/monthly_data.csv')
    return df.to_string(index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    user_message = request.json['message']
    data_input = input_data()
    response = user_message + data_input
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
