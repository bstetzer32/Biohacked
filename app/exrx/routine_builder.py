from ..models import db, Routine, Workout, WorkoutExercise, Exercise, Scheme, User

def routine_builder(questionnaire):
    if questionnaire.goal == 'increase':
        routine = Routine(
            user_id = questionnaire.user_id,
            questionnaire_id = questionnaire.id,
            workouts = [
                Workout(
                    order=1
                ),
                Workout(
                    order=2
                ),
                Workout(
                    order=3
                ),
                Workout(
                    order=4
                ),
                Workout(
                    order=5
                )
            ]
        )
        db.add(routine)
        db.commit()
        pass
    if questionnaire.goal == 'decrease':
        pass
    if questionnaire.goal == 'maintain':
        pass