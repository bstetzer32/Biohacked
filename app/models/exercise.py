from .db import db

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    movement_id = db.Column(db.Integer, db.ForeignKey("movements.id"), nullable = False)
    modality = db.Column(db.String(50), nullable = False)
    api_id = db.Column(db.Integer, unique=True)
    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise")
    movement = db.relationship("Movement", back_populates="exercises")
    
    def to_dict(self):

        return {
            "id": self.id,
            "movement": self.movement.name,
            "modality": self.modality,
            "api_id": self.api_id
        }