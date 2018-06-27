from flask import Flask, render_template, send_file
from scrap import Scrap
from db_connection import DatabaseController
from steamcommunitytop import SteamScrap
import _thread
import strings
app = Flask(__name__)

name = "Flask App"


@app.route('/')
def index():
    SteamScrapper = SteamScrap()
    database = DatabaseController()
    SteamScrapper.initialization()
    allitems = SteamScrapper.get_objects()
    item = SteamScrapper.get_object()
    _thread.start_new_thread(database.insert_into_items, (allitems, ))
    return render_template('index.html', name=name, item=item)


@app.route('/steamsales')
def about():
    Scrapper = Scrap()
    database = DatabaseController()
    Scrapper.initialization()
    items = Scrapper.get_objects()
    _thread.start_new_thread(database.insert_into_games, (items, ))
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