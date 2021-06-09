from sqlalchemy.orm import backref
from .db import db
from .scheme_set_rep import scheme_set_rep


class Scheme(db.Model):
    __tablename__ = 'schemes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    sets = db.Column(db.Integer)
    reps = db.Column(db.String(50))
    tempo = db.Column(db.String(50))
    time = db.Column(db.Integer)
    rest = db.Column(db.Integer)
    base_set = db.Column(db.Integer)
    modifier = db.Column(db.Float)
    direction = db.Column(db.Boolean)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="scheme")
    # set_reps = db.relationship('SetRep', secondary=scheme_set_rep,
    #                            backref=db.backref('schemes'))

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "sets": self.sets,
            "reps": self.reps,
            "tempo": self.tempo,
            "time": self.time,
            "rest": self.rest,
            "base_set": self.base_set,
            "modifier": self.modifier,
            "direction": self.direction
        }

    def to_exercise_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "sets": self.sets,
            "reps": self.reps,
            "tempo": self.tempo,
            "time": self.time,
            "rest": self.rest,
            "base_set": self.base_set,
            "modifier": self.modifier,
            "direction": self.direction
        }
