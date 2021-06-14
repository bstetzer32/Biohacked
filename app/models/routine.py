import re
from .db import db
import datetime


class Routine(db.Model):
    __tablename__ = 'routines'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    questionnaire_id = db.Column(
        db.Integer, db.ForeignKey("questionnaires.id"))
    created_at = db.Column(
        db.DateTime(), default=datetime.datetime.now(), nullable=False)
    user = db.relationship("User", back_populates="routines")
    questionnaire = db.relationship("Questionnaire", back_populates="routine")
    workouts = db.relationship(
        "Workout", back_populates="routine", cascade="all, delete")
    results = db.relationship("RoutineResult",
                              back_populates="routine", cascade="all, delete")

    def to_dict(self):

        return {
            "id": self.id,
            "user_id": self.user_id,
            "questionnaire_id": self.questionnaire_id,
            "created_at": self.created_at
        }

    def to_user_dict(self):
        results = sorted([result.to_routine_dict()
                         for result in self.results],
                         key=lambda i: i['created_at'])

        return {
            "id": self.id,
            "questionnaire": self.questionnaire.to_routine_dict(),
            "created_at": self.created_at,
            "workouts": [workout.to_routine_dict() for workout in self
                         .workouts],
            "results": results
        }
