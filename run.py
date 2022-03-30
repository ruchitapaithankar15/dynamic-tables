
from flask import Flask, g, jsonify, render_template, request

from db import Database

DATABASE_PATH = 'bikes.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = Database(DATABASE_PATH)
    return db


@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about2')
def about2():
    data = {
        'related': [
            {'name': 'Services', 'url': 'https://drexel.edu/campusservices/studentCenters/services/'},
            {'name': 'We Rent Bikes', 'url': 'https://drexel.edu/campusservices/studentCenters/services/BikeShare/'},
            {'name': 'Membership Agreement', 'url': 'https://drexel.qualtrics.com/jfe/form/SV_af8SeOsULUqCIVn'}
        ]
    }
    return render_template('about2.html', data=data)

@app.route('/rent')
def bikes():
    return render_template('rent.html')


def generate_response(args):
    bikes = get_db().get_bikes()
    return jsonify(bikes)


@app.route('/api/get_bikes', methods=['GET'])
def api_get_bikes():
    return generate_response(request.args)


@app.route('/api/update_bikes', methods=['POST'])
def api_bikes():
    id = request.form.get('id')
    available = request.form.get('available')
    get_db().update_bikes(id, available)
    return generate_response(request.form)

@app.route('/api/reset_bikes', methods=['POST'])
def api_reset_bikes():
    available = request.form.get('available')
    get_db().reset_bikes(available)
    return generate_response(request.form)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
