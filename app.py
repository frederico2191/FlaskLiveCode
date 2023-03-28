from flask import Flask, jsonify, request
from PersonModel import db, PersonModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyDBTest.db'
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def myRootMethod():
    return "Hello World"

@app.route("/api/person/")
def getPersons():
    persons = PersonModel.query.all()
    result = []
    for person in persons:
        result.append(person.serialize())
    return jsonify(result)


@app.route("/api/person/<int:id>")
def getPerson(id):
    if id == 10:
        content = {"details": "Hey, there has been an error on your request"}
        resp = jsonify(content)
        resp.status_code = 404
        return resp
    person = {"id":id, "name":"Carlos Muniz"}
    return jsonify(person)

@app.route("/api/person/<int:id>", methods=['DELETE'])
def deletePerson(id):
    if id == 10:
        content = {"details": "Hey, there has been an error on your request"}
        resp = jsonify(content)
        resp.status_code = 404
        return resp
    return '',204

@app.route("/api/person/", methods=['POST'])
def addPerson():
    body = request.get_json()
    myobj = PersonModel()
    myobj.name = body['name']
    db.session.add(myobj)
    db.session.commit()
    return '',204

@app.route("/api/person/", methods=['PUT'])
def updatePerson():
    body = request.get_json()
    resposeBody = {"id":body['id'],"name": body['name']+ " Update!!!"}
    return jsonify(resposeBody)



app.run(host='0.0.0.0', port='1234')
