from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.forms import QuestionnaireForm
from app.models import Routine, Questionnaire, db, questionnaire
from ..exrx.exrx_query import exrx_query

exercise_routes = Blueprint('exercises', __name__)


# @login_required
@exercise_routes.route('/<int:id>')
def get_info(id):
    info = exrx_query('exerciseids', f'[{id}]')
    info = info['exercises'][0]
    img = info['Recommend_Image']
    info = {
        "name": info['Exercise_Name_Complete'],
        "target_muscle": info['Target_Muscle_Group'],
        "preparation": info['Instructions_Preparation'],
        "execution": info['Instructions_Execution'],
        "image": info[f'Larg_Img_{img}'],
        "video": info['video_src'],
        "url": info['URL']
    }
    return info
