from flask import Flask, render_template, send_file
from scrapper.SteamSalesScrap import Scrap
from extensions.DBConnection import DatabaseController
from scrapper.SteamCommunityScrap import SteamScrap
from scrapper.CurrentPlayerCountsScrap import CurrentPlayerCount
import _thread
from strings import strings

app = Flask(__name__)

name = "Flask App"

dbcontroller = DatabaseController()


@app.route('/')
def index():
    CSV = "/return-file/top-common-items"
    SteamScrapper = SteamScrap()
    SteamScrapper.initialization()
    allitems = SteamScrapper.get_objects()
    _thread.start_new_thread(dbcontroller.insert_into_items, (allitems, ))
    return render_template('index.html', name=name, item=allitems[0], link=CSV)


@app.route('/steamsales')
def about():
    CSV = "/return-file/sales"
    Scrapper = Scrap()
    Scrapper.initialization()
    items = Scrapper.get_objects()
    _thread.start_new_thread(dbcontroller.insert_into_games, (items, ))
    return render_template('steamsales.html', items=items, link=CSV)


@app.route('/pubg')
def pubg():
    CSV = "/return-file/top-multi-player-games"
    currentplayers = CurrentPlayerCount()
    currentplayers.initialization()
    items = currentplayers.get_objects()
    _thread.start_new_thread(dbcontroller.insert_into_current_players, (items, ))
    return render_template('pubg.html', items=items, link=CSV)


# correct
@app.route('/return-file/sales')
def return_file_sales():
    return send_file(strings.send_file_path_sales, as_attachment=True)


# incorrect
@app.route('/return-file/top-common-items')
def return_file_top_common_items():
    return send_file(strings.send_file_path_common_items, as_attachment=True)


# incorrect
@app.route('/return-file/top-multi-player-games')
def return_file_multiplayergames():
    return send_file(strings.send_file_path_current_players, as_attachment=True)


@app.route('/file-downloads/')
def file_download():
    return render_template('downloads.html')


if __name__ == '__main__':
    app.run(debug=True)