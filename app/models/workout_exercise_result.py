from .db import db


class WorkoutExerciseResult(db.Model):
    __tablename__ = 'workout_exercise_results'

    id = db.Column(db.Integer, primary_key=True)
    set = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    load = db.Column(db.Integer)
    time = db.Column(db.Integer)
    rest = db.Column(db.Integer)
    workout_exercise_id = db.Column(
        db.Integer, db.ForeignKey("workout_exercises.id"))

    workout_exercise = db.relationship("WorkoutExercise",
                                       back_populates="results")

    def to_dict(self):

        return {
            "id": self.id,
            "set": self.set,
            "reps": self.reps,
            "load": self.load,
            "time": self.time,
            "rest": self.rest,
            "workout_exercise_id": self.workout_exercise_id,
        }

    def to_exercise_dict(self):

        return {
            "id": self.id,
            "set": self.set,
            "reps": self.reps,
            "load": self.load,
            "time": self.time,
            "rest": self.rest,
            "scheme": self.workout_exercise.scheme.name
        }
