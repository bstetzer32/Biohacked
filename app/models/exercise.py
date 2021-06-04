from .db import db

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable = False)
    muscle = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)
    api_id = db.Column(db.Integer, unique=True)
    
    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise")
    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "muscle": self.muscle,
            "type": self.type,
            "api_id": self.api_id
        }