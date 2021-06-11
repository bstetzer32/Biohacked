from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import WorkoutExercise, WorkoutExerciseResult, db

result_routes = Blueprint('results', __name__)


@login_required
@result_routes.route('', methods=['POST'])
def submit_results():
    data = request.json['results']
    print(data)
    for exercise_id in data.keys():
        checked = True
        result = data[exercise_id]['results']
        print(result)
        for set in result:
            print(result[set])
            if result[set]['checked'] is False:
                checked = False
        if not checked:
            continue
        exercise = WorkoutExercise.query.get(exercise_id)
        for set in result.keys():
            last_set = result[set]
            print('------', last_set, set)
            exercise_result = WorkoutExerciseResult(
                set=int(set) + 1,
                reps=(result[set]['reps'] if 'reps' in result[set] else None),
                load=(result[set]['load'] if 'load' in result[set] else None),
                time=(result[set]['time'] if 'time' in result[set] else None),
                rest=(result[set]['rest'] if 'rest' in result[set] else None),
                workout_exercise_id=exercise_id
            )
            db.session.add(exercise_result)
        if 'load' in last_set and last_set['load'] != 0:
            exercise.max = float(last_set['load'])*(36/(37-last_set['reps']))
            db.session.add(exercise)
    db.session.commit()
    return{}
