from flask import Flask, request, render_template

app = Flask(__name__)

users = {
    'admin': 'admin',
    'user1': 'user1',
    'alex': 'Jshdj23',
    'nag231': 'M34mdjL'
}


@app.route('/home')
def home():
    return 'HOME'


@app.route('/test')
def test():
    a = 5
    b = 10
    return {
        'a': a,
        'b': b,
        'sum': a + b
    }


@app.route('/users/get_names', methods=['GET'])
def get_names():
    return {
        'names': list(users.keys())
    }


@app.route('/users/get_passwords', methods=['GET'])
def get_passwords():
    return {
        'names': list(users.values())
    }


@app.route('/users', methods=['GET'])
def get_users():
    return users


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return {
                'status': 'ok',
                'user': {
                    'username': username,
                    'password': password
                },
                'message': 'Добро пожаловать!'
            }
        else:
            return {
                'status': 'error',
                'message': 'Неверный логин или пароль'
            }

    return render_template('login.html')


app.run()
