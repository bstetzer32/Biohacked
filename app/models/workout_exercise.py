from .db import db

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key = True)
    max = db.Column(db.Integer, nullable=False)
    scheme_id = db.Column(db.Integer, db.ForeignKey("schemes.id"))
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable = False)

    scheme = db.relationship("Scheme", back_populates="workout_exercises")
    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")
    results = db.relationship("WorkoutExerciseResult", back_populates="workout_exercise")

    def to_dict(self):

        return {
            "id": self.id,
            "max": self.name,
            "workout_id": self.workout_id,
            "exercise_id": self.exercise_id
        }