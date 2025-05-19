from flask import Flask, render_template
import requests

app = Flask(__name__)
age_url = 'https://api.agify.io'
gender_url = 'https://api.genderize.io'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/guess/<name>')
def guess(name):
    gender_params = {
        'name': name
    }
    gender_content = requests.get(gender_url, params=gender_params)
    gender = gender_content.json()['gender']

    age_params = {
        'name': name
    }
    age_content = requests.get(age_url, params=age_params)
    age = age_content.json()['age']

    return render_template('index.html', gender=gender, age=age, name=name)


if __name__ == '__main__':
    app.run(debug=True)
