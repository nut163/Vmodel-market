```python
from flask import Flask, render_template, request, redirect, url_for
from onboarding_system.signup import signupUser
from onboarding_system.upload_voice_models import loginUser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login_signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    signupUser(username, password)
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    loginUser(username, password)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```
This code creates a Flask web application with a home route that renders a login/signup screen. It also includes routes for handling POST requests from the signup and login forms. The signup and login functions from the onboarding_system module are used to handle user registration and authentication.