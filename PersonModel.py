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