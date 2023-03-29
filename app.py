from flask import Flask, jsonify, request
from PersonModel import db, PersonModel, Films, Character, Planets

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyDBTest.db'
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def myRootMethod():
    return "This is home!"

@app.route("/api/films/", methods=['GET'])
def getFilms():
    films = Films.query.all()
    result = []
    for film in films:
        characters = []
        filtered_character= Character.query.filter_by(film_id = film.id)
        for c in filtered_character:
            characters.append("/people/"+c.people_id)
        result.append({'id': film.id, 'characters': characters})
    return jsonify(result)

@app.route("/api/films/", methods=['POST'])
def addFilm():
    body = request.get_json()
    myobj = Films()
    myobj.title = body['title']
    db.session.add(myobj)
    db.session.commit()
    return '',204


@app.route("/api/people/<int:people_id>", methods=['GET'])
def getPerson(id):
    people = People.query.all()
    content = []
    for i in people:
        if i == id:
            content.append(people)
        resp = jsonify(content)
        resp.status_code = 404
        return resp
    return jsonify(person)

@app.route("/api/person/<int:people_id>", methods=['DELETE'])
def deletePerson(id):
    if Person.query.get(id) != None:
        person = Person.query.get(id)
        db.session.delete(person)
        db.session.commit()
        return 'deleted!',204
    else:
        content = {"details": "Hey, there has been an error on your request"}
        resp = jsonify(content)
        resp.status_code = 404
        return resp
   

@app.route("/api/person/<int:people_id>", methods=['PUT'])
def updatePerson(id,name):
    person = Person.query.get(id)
    person.name = name
    db.session.commit()
    body = request.get_json()
    resposeBody = {"id":body['id'],"name": body['name']+ " Update!!!"}
    return jsonify(resposeBody)



app.run(host='0.0.0.0', port='1234', debug=True)
