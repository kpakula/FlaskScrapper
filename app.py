from flask import Flask, render_template, send_file
from scrap import Scrap
import strings
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


@app.route('/return-file/')
def return_file():
    return send_file(strings.send_file_path, as_attachment=True)


@app.route('/file-downloads/')
def file_download():
    return render_template('downloads.html')


if __name__ == '__main__':
    app.run(debug=True)