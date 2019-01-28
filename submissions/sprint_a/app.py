from sprint_a import app
import flask


@app.route('/')
def generate_epithets():
    epithets_dict = {"epithets": []}
    return flask.jsonify(epithets_dict)


@app.route('/vocabulary')
def vocabulary():
    vocab_dict = {"vocabulary": {}}
    return flask.jsonify(vocab_dict)
