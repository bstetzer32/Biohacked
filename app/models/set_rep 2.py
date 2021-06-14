from .db import db


class SetRep(db.Model):
    __tablename__ = 'set_reps'

    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer)
    modifier = db.Column(db.Float)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="scheme")

    def to_dict(self):

        return {
            "id": self.id,
            "reps": self.reps,
            "modifier": self.modifier,
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
