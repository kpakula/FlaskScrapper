from flask import Flask, render_template
from scrap import Scrap
app = Flask(__name__)

name = "Flask App"


@app.route('/')
def index():
    return render_template('index.html', name=name)


@app.route('/steamsales')
def about():
    Scrapper = Scrap()
    Scrapper.initialization()
    items = Scrapper.get_objects()
    return render_template('steamsales.html', items=items)


@app.route('/pubg')
def pubg():
    return render_template('pubg.html')



if __name__ == '__main__':
    app.run(debug=True)