from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.forms import QuestionnaireForm
from app.models import Routine, Questionnaire, db, questionnaire
from ..exrx.routine_builder import routine_builder

questionnaire_routes = Blueprint('questionnaire', __name__)


@questionnaire_routes.route('', methods=['POST'])
@login_required
def post_questionnaire():
    form = QuestionnaireForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        print('pass')
        questionnaire = Questionnaire(
            user_id=form.data['user_id'],
            parq1=form.data['parq1'],
            parq2=form.data['parq2'],
            parq3=form.data['parq3'],
            parq4=form.data['parq4'],
            parq5=form.data['parq5'],
            parq6=form.data['parq6'],
            parq7=form.data['parq7'],
            barbell=form.data['barbell'],
            dumbbell=form.data['dumbbell'],
            cable=form.data['cable'],
            lever=form.data['lever'],
            goal=form.data['goal'],
            height=form.data['height'],
            weight=form.data['weight'],
            age=form.data['age']
        )
        db.session.add(questionnaire)
        db.session.commit()
        routine_builder(questionnaire)
        return {}
    print('fail')
    return {}


@questionnaire_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_routine(id):
    routine = Routine.query.get(id)
    if routine.user_id == current_user.id:
        db.session.delete(routine)
        db.session.commit()
        return {}
    else:
        return {"errors": ["It doesn't look like this routine is yours. If you"
                + "feel you have received this email in error, please email"
                + "biohackedfitness@gmail.com for support"]}
