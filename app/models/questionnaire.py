from .db import db
import datetime

class Questionnaire(db.Model):
    __tablename__ = 'questionnaires'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    parq1 = db.Column(db.String(3), nullable = False)
    parq2 = db.Column(db.String(3), nullable = False)
    parq3 = db.Column(db.String(3), nullable = False)
    parq4 = db.Column(db.String(3), nullable = False)
    parq5 = db.Column(db.String(3), nullable = False)
    parq6 = db.Column(db.String(3), nullable = False)
    parq7 = db.Column(db.String(3), nullable = False)
    barbells = db.Column(db.String(3), nullable = False)
    dumbbells = db.Column(db.String(3), nullable = False)
    cables = db.Column(db.String(3), nullable = False)
    levers = db.Column(db.String(3), nullable = False)
    goal = db.Column(db.String(8), nullable = False)
    height = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now())

    user = db.relationship("User", back_populates="questionnaires")
    routine = db.relationship("Routine", back_populates="questionnaire")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "parq1": self.parq1,
            "parq2": self.parq2,
            "parq3": self.parq3,
            "parq4": self.parq4,
            "parq5": self.parq5,
            "parq6": self.parq6,
            "parq7": self.parq7,
            "barbells": self.barbells,
            "dumbbells": self.dumbbells,
            "cables": self.cables,
            "levers": self.levers,
            "goal": self.goal,
            "height": self.height,
            "weight": self.weight,
            "age": self.age,
            "created_at": self.created_at
        }