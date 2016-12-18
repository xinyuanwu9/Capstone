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

    # beer_inp = None

    # if form.validate():
    print "456"
    if request.method == "POST" and "beer_inp" in request.form:
        beer_inp = request.form["beer_inp"]

        cb_rec = get_similar_beers(beer_inp, beer_list, index)
        print str(cb_rec)

        return render_template("content.html", cb_rec=cb_rec)

    else:
        # print "123"
        return render_template("content.html")

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