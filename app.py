from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

def is_valid_ip(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, ip)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    ip = request.form['ip']

    if not is_valid_ip(ip):
        return render_template('result.html', error="Invalid IP Address")

    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    if data['status'] == 'fail':
        return render_template('result.html', error="IP not found")

    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)