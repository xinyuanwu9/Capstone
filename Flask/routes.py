from flask import Flask, render_template, request, jsonify, url_for
from model.CB.content_based_recommendation import *
import pickle

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/viewbeers.html")
def viewbeers():
    return render_template("viewbeers.html")

@app.route("/content.html", methods=['GET', 'POST'])
def content():
    with open("./model/CB/beer_list.p", "rb") as bf:
        beer_list = pickle.load(bf)
    with open("./model/CB/index.p", "rb") as idxf:
        index = pickle.load(idxf)
    with open("./model/CB/corpus_tfidf.p", "rb") as corpus_t:
        corpus_tfidf = pickle.load(corpus_t)
    with open("./model/CB/textDict.p", "rb") as tD:
        textDict = pickle.load(tD)

    if request.method == "GET":
        return render_template("content.html", beerlist=beer_list)

    beer_inp = None
    if request.method == "POST" and "beer_inp" in request.form:
        beer_inp = request.form["beer_inp"]
        if beer_inp == '':
            return render_template("content.html", beerlist=beer_list)
        else:
            cb_rec = get_similar_beers(beer_inp, beer_list, index)
            key_words = get_beer_keywords(beer_inp, corpus_tfidf, beer_list, textDict, ntop=10)
            key_words = map(lambda x: x.decode('utf-8', 'ignore').encode('ascii', 'ignore'), key_words)
            key_words = ', '.join(key_words)
            return render_template("content.html", beerlist=beer_list, cb_rec=cb_rec, key_words=key_words)

@app.route("/collab.html")
def collab():
    return render_template("collab.html")


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    #query = db_session.query(Movie.title).filter(Movie.title.like('%' + str(search) + '%'))
    #results = [mv[0] for mv in query.all()]
    results = ['Beer1', 'Wine1', 'Soda1', 'a', 'b']
    return jsonify(matching_results=results)

if __name__ == "__main__":
  app.run(debug=True)