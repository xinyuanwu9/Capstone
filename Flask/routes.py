from flask import Flask, render_template, request, jsonify, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/viewbeers.html")
def viewbeers():
    return render_template("viewbeers.html")

@app.route("/content.html")
def content():
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