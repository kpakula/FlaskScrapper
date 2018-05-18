from flask import Flask, render_template

app = Flask(__name__)

name = "Flask App"


@app.route('/')
def index():
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)