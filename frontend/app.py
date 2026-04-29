import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
API_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    response = requests.get(f"{API_URL}/doctors")
    doctors = response.json()
    return render_template('index.html', doctors=doctors)

@app.route('/create', methods=['GET', 'POST'])
def create_doctor():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'profession': request.form.get('profession'),
            'age': request.form.get('age'),
            'available': request.form.get('available')=="on",
        }
        response = requests.post(f"{API_URL}/doctors", json=data)
        if response.status_code == 201:
            return redirect('/')
        return render_template("form.html", error=response.text)

    return render_template("form.html")