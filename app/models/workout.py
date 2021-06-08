from .db import db


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    routine_id = db.Column(
        db.Integer, db.ForeignKey("routines.id"), nullable=False)

    routine = db.relationship("Routine", back_populates="workouts")

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="workout")

    def to_dict(self):

        return {
            "id": self.id,
            "order": self.order,
            "routine_id": self.routine_id
        }
