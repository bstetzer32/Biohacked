from .db import db
import datetime
from collections import OrderedDict


class RoutineResult(db.Model):
    __tablename__ = 'routine_results'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime(), default=datetime.datetime.now(), nullable=False)
    routine_id = db.Column(
        db.Integer, db.ForeignKey("routines.id"), nullable=False)
    routine = db.relationship("Routine", back_populates="results")
    results = db.relationship("WorkoutExerciseResult",
                              back_populates="routine_result")

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

    def to_routine_dict(self):
        results = [result.to_exercise_dict() for result in self.results]
        return {
            "id": self.id,
            "created_at": self.created_at,
            "results": results,
        }
