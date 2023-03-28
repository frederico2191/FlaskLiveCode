from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PersonModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    planets = db.Column(db.String(2500), nullable=False, default="No info")
    characters = db.Column(db.String(2500), nullable=True)
    created = db.Column(db.Integer, nullable=False, default="No info")
    edited = db.Column(db.Integer, nullable=False, default="No info")
    producer = db.Column(db.String(30), nullable=False, default="No info")
    director = db.Column(db.String(30), nullable=False, default="No info")
    realease_date = db.Column(db.Integer, nullable=False, default="No info")
    opening_crawl = db.Column(db.String(250), nullable=False, default="No info")
    url = db.Column(db.String(250), nullable=False, default="No info")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title
        }


class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, ForeignKey('films.id'))
    film = relationship(Films)
    people_id = db.Column(db.Integer, ForeignKey('people.id'))
    people = relationship(People)


class People(Base):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(30), nullable=False)
    eye_color = db.Column(db.String(30), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    # homeworld = db.Column(db.String(250), nullable=False)
    # url = db.Column(db.String(250), nullable=False)


# class Planets(Base):
#     __tablename__ = 'planets'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(db.Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     url = Column(String(2500), nullable=False)
#     climate = Column(String(250), nullable=False)
#     terrain = Column(String(250), nullable=False)

#     # film_id= Column(db.Integer, ForeignKey('films.id'))
#     # film = relationship(Films)

#     # planets_id = Column(Integer, ForeignKey('films.id'))
#     # planets = relationship(Films)

# class PlanetsInFilms(Base):
#     __tablename__ = 'planetsInFilms'
#     id = Column(Integer, primary_key=True)
#     planets_id = Column(Integer, ForeignKey('planets.id'))
#     planets = relationship(Planets)
#     film_id = Column(Integer, ForeignKey('films.id'))
#     film = relationship(Films)


# class Vehicles(Base):
#     __tablename__ = 'vehicles'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     url = Column(String(2500), nullable=False)
#     model = Column(String(2500), nullable=False)
#     vehicle_class = Column(String(2500), nullable=False)
#     manufacturer = Column(String(2500), nullable=False)
#     cost_in_credits = Column(String(2500), nullable=False)
#     length = Column(Integer, nullable=False)
#     crew = Column(String(2500), nullable=False)
#     passangers = Column(Integer, nullable=False)
#     max_atmosphering_speed = Column(Integer, nullable=False)
#     cargo_capacity = Column(Integer, nullable=False)
#     max_atmosphering_speed = Column(String(2500), nullable=False)


#     # film_id= Column(Integer, ForeignKey('films.id'))
#     # film = relationship(Films)






# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
# class Character(Base):
#     __tablename__ = 'character'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
#     homeworld_id = Column(Integer, ForeignKey('planets.id'))
#     homeworld = relationship(Planets)
#     film_id = Column(Integer, ForeignKey('films.id'))
#     film = relationship(Films)
#     person_id = Column(Integer, ForeignKey('people.id'))
#     person = relationship(People)


# class VehiclesInFilms(Base):
#     __tablename__ = 'vehiclesInFilms'
#     id = Column(Integer, primary_key=True)
#     vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
#     vehicles = relationship(Vehicles)
#     film_id = Column(Integer, ForeignKey('films.id'))
#     film = relationship(Films)


# class Favorites(Base):
#     __tablename__ = 'favorites'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     username = Column(String(250), nullable=False)
#     fav_planet_id = Column(Integer, ForeignKey('planets.id'))
#     planet = relationship(Planets)
#     fav_vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
#     vehicle = relationship(Films)
#     fav_person_id = Column(Integer, ForeignKey('people.id'))
#     person = relationship(People)




    # def to_dict(self):
    #     return {}