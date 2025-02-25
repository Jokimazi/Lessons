from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/test')
def test():
    a = 123
    return {
        'a': a,
        'dinaxy': 1488
    }

@app.route('/calc')
def calc():
    pass

app.run()
