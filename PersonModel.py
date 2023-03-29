from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    planets = db.Column(db.String(2500), nullable=True)
    people = db.Column(db.String(2500), nullable=True)
    created = db.Column(db.Integer, nullable=True)
    edited = db.Column(db.Integer, nullable=True)
    producer = db.Column(db.String(30), nullable=True)
    director = db.Column(db.String(30), nullable=True)
    realease_date = db.Column(db.Integer, nullable=True)
    opening_crawl = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(30), nullable=True)
    eye_color = db.Column(db.String(30), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    homeworld = db.Column(db.String(250), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "title": self.name
        }


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    model = db.Column(db.String(2500), nullable=True)
    vehicle_class = db.Column(db.String(2500), nullable=True)
    manufacturer = db.Column(db.String(2500), nullable=True)
    cost_in_credits = db.Column(db.String(2500), nullable=True)
    length = db.Column(db.Integer, nullable=True)
    crew = db.Column(db.String(2500), nullable=True)
    passangers = db.Column(db.Integer, nullable=True)
    max_atmosphering_speed = db.Column(db.Integer, nullable=True)
    cargo_capacity = db.Column(db.Integer, nullable=True)
    max_atmosphering_speed = db.Column(db.String(2500), nullable=True)
    # url = db.Column(db.String(2500), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "title": self.name
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(2500), nullable=True)
    climate = db.Column(db.String(250), nullable=True)
    terrain = db.Column(db.String(250), nullable=True)
    film_id= db.Column(db.Integer, ForeignKey('films.id'))
    film = relationship(Films)

class PlanetsInFilms(db.Model):
    __tablename__ = 'planetsInFilms'
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    film_id = db.Column(db.Integer, ForeignKey('films.id'))
    film = relationship(Films)

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, ForeignKey('films.id'))
    film = relationship(Films)
    people_id = db.Column(db.Integer, ForeignKey('people.id'))
    people = relationship(People)

class Character(db.Model):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship(Planets)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship(Films)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(People)


class VehiclesInFilms(db.Model):
    __tablename__ = 'vehiclesInFilms'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship(Films)


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    fav_planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    fav_vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Films)
    fav_person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(People)
