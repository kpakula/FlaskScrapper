from flask import Flask, render_template

app = Flask(__name__)

name = "Flask App"


@app.route('/')
def index():
    return render_template('index.html', name=name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/pubg')
def pubg():
    return render_template('pubg.html')


if __name__ == '__main__':
    app.run(debug=True)