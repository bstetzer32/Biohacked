from .db import db
from collections import OrderedDict


class WorkoutExerciseResult(db.Model):
    __tablename__ = 'workout_exercise_results'

    id = db.Column(db.Integer, primary_key=True)
    set = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    load = db.Column(db.Integer)
    time = db.Column(db.Integer)
    rest = db.Column(db.Integer)
    routine_result_id = db.Column(
        db.Integer, db.ForeignKey("routine_results.id"))
    workout_exercise_id = db.Column(
        db.Integer, db.ForeignKey("workout_exercises.id"))
    routine_result = db.relationship(
        "RoutineResult", back_populates="results")
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
        results = OrderedDict()
        results = {
            "id": self.id,
            "set": self.set,
            "reps": self.reps,
            "load": self.load,
            "time": self.time,
            "rest": self.rest,
            "scheme": self.workout_exercise.scheme.name,
            "exercise": self.workout_exercise.to_result_dict()
        }
        return results
