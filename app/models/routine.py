from .db import db
import datetime

class Routine(db.Model):
    __tablename__ = 'routines'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("questionnaires.id"))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable = False)
    user = db.relationship("User", back_populates="routines")
    questionnaire = db.relationship("Questionnaire", back_populates="routine")
    workouts = db.relationship("Workout", back_populates="routine")

    def to_dict(self):

        return {
            "id": self.id,
            "user_id": self.user_id,
            "questionnaire_id": self.questionnaire_id,
            "created_at": self.created_at
        }