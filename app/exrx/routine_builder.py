from app.models import workout_exercise
from ..models import db, Routine, Workout, WorkoutExercise, Exercise, Scheme
from sqlalchemy import or_
from flask import jsonify


def routine_builder(questionnaire):
    exercises = Exercise.query.filter(or_(Exercise
                                      .modality == questionnaire.barbell,
                                          Exercise
                                      .modality == questionnaire.dumbbell,
                                          Exercise
                                      .modality == questionnaire.cable,
                                          Exercise
                                      .modality == questionnaire.lever,
                                          Exercise
                                      .modality == "bodyweight",)).all()
    print(exercises)
    movements = {}
    for exercise in exercises:
        print(movements)
        if exercise.movement_id not in movements:
            movements[exercise.movement_id] = exercise.id
    if questionnaire.goal == 'increase':
        routine = Routine(
            user_id=questionnaire.user_id,
            questionnaire_id=questionnaire.id,
            workouts=[
                Workout(
                    order=1,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[6])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[7])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[11])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[1])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[21])
                                         if 21 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[24])
                                         if 24 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[23])
                                         if 23 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[26])
                                         if 26 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[22])
                                         if 22 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[25])
                                         if 25 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=2,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[8])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[9])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[10])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[2])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[27])
                                         if 27 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[28])
                                         if 28 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[31])
                                         if 31 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[30])
                                         if 30 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[29])
                                         if 29 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[32])
                                         if 32 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=3,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[11])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[12])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[13])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[3])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[33])
                                         if 33 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[34])
                                         if 34 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[35])
                                         if 35 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[36])
                                         if 36 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[37])
                                         if 37 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[38])
                                         if 38 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=4,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[14])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[15])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[13])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[4])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[28])
                                         if 28 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[39])
                                         if 39 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[40])
                                         if 40 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[41])
                                         if 41 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[43])
                                         if 43 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[42])
                                         if 42 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=5,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[16])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[17])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[6])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[5])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[44])
                                         if 44 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[45])
                                         if 45 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[46])
                                         if 46 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[47])
                                         if 47 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[48])
                                         if 48 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[49])
                                         if 49 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                )
            ]
        )
        db.session.add(routine)
        db.session.commit()
        return routine
    if questionnaire.goal == 'decrease':
        routine = Routine(
            user_id=questionnaire.user_id,
            questionnaire_id=questionnaire.id,
            workouts=[
                Workout(
                    order=1,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[6])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[7])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[11])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[1])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[21])
                                         if 21 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[23])
                                         if 23 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[22])
                                         if 22 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[33])
                                         if 33 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[34])
                                         if 34 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[35])
                                         if 35 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=2,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[8])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[9])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[10])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[2])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[27])
                                         if 27 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[28])
                                         if 28 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[29])
                                         if 29 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[39])
                                         if 39 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[40])
                                         if 40 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[41])
                                         if 41 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=3,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[11])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[12])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[13])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[3])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[33])
                                         if 33 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[34])
                                         if 34 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[35])
                                         if 35 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[21])
                                         if 21 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[23])
                                         if 23 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[22])
                                         if 22 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=4,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[14])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[15])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[13])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[4])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[39])
                                         if 39 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[40])
                                         if 40 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[41])
                                         if 41 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[27])
                                         if 27 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[28])
                                         if 28 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[29])
                                         if 29 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=5,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[16])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[17])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[6])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[5])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[44])
                                         if 44 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[45])
                                         if 45 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[46])
                                         if 46 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[47])
                                         if 47 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[48])
                                         if 48 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[49])
                                         if 49 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                )
            ]
        )
        db.session.add(routine)
        db.session.commit()
        return routine
    if questionnaire.goal == 'maintain':
        routine = Routine(
            user_id=questionnaire.user_id,
            questionnaire_id=questionnaire.id,
            workouts=[
                Workout(
                    order=1,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[6])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[7])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[11])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[1])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[21])
                                         if 21 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[23])
                                         if 23 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[22])
                                         if 22 in movements else 1)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=2,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[8])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[9])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[10])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[2])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[27])
                                         if 27 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[28])
                                         if 28 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[29])
                                         if 29 in movements else 2)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=3,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[11])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[12])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[13])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[3])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[33])
                                         if 33 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[34])
                                         if 34 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[35])
                                         if 35 in movements else 3)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=4,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[14])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[15])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[13])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[4])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[39])
                                         if 39 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[40])
                                         if 40 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[41])
                                         if 41 in movements else 4)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                ),
                Workout(
                    order=5,
                    workout_exercises=[
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=18
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=19
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=20
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[16])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[17])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=9,
                            exercise_id=int(movements[6])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=10,
                            exercise_id=int(movements[5])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[45])
                                         if 45 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[46])
                                         if 46 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=1,
                            exercise_id=(int(movements[47])
                                         if 47 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=4,
                            exercise_id=(int(movements[48])
                                         if 48 in movements else 5)
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=105
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=7,
                            exercise_id=106
                        ),
                        # WorkoutExercise(
                        #     max=0,
                        #     scheme_id=7,
                        #     exercise_id=107
                        # ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=108
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=8,
                            exercise_id=109
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=11,
                            exercise_id=int(movements[55])
                        ),
                        WorkoutExercise(
                            max=0,
                            scheme_id=14,
                            exercise_id=int(movements[56])
                        )
                    ]
                )
            ]
        )
        db.session.add(routine)
        db.session.commit()
        return routine
