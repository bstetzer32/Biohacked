from .db import db

class Movement(db.Model):
    __tablename__ = 'movements'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable = False)
    muscle_group = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)
    exercises = db.relationship("Exercise", back_populates="movement")
    
    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "muscle_group": self.muscle_group,
            "type": self.type,
            "exercises": self.exercises.to_dict()
        }