from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.forms import QuestionnaireForm
from app.models import User, Questionnaire, db

questionnaire_routes = Blueprint('questionnaire', __name__)

@questionnaire_routes.route('', methods=['POST'])
@login_required
def post_questionnaire():
    form = QuestionnaireForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        questionnaire = Questionnaire(
            user_id=form.data['user_id'],
            parq1=form.data['parq1'],
            parq2=form.data['parq2'],
            parq3=form.data['parq3'],
            parq4=form.data['parq4'],
            parq5=form.data['parq5'],
            parq6=form.data['parq6'],
            parq7=form.data['parq7'],
            barbells=form.data['barbells'],
            dumbbells=form.data['dumbbells'],
            cables=form.data['cables'],
            levers=form.data['levers'],
            goal=form.data['goal'],
            height=form.data['height'],
            weight=form.data['weight'],
            age=form.data['age']
        )
        db.session.add(questionnaire)
        db.session.commit()