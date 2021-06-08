from app.models import db, Exercise


def seed_exercises():
    chest_warmup = Exercise(
        movement_id=1,
        modality="bodyweight",
        api_id=616
    )
    leg_warmup = Exercise(
        movement_id=2,
        modality="bodyweight",
        api_id=916
    )
    shoulder_warmup = Exercise(
        movement_id=3,
        modality="bodyweight",
        api_id=1911
    )
    back_warmup = Exercise(
        movement_id=4,
        modality="bodyweight",
        api_id=790
    )
    arm_warmup = Exercise(
        movement_id=5,
        modality="bodyweight",
        api_id=311
    )
    pectoralis_major_stretch = Exercise(
        movement_id=6,
        modality="bodyweight",
        api_id=1242
    )
    pectoralis_minor_stretch = Exercise(
        movement_id=7,
        modality="bodyweight",
        api_id=1243
    )
    quadriceps_stretch = Exercise(
        movement_id=8,
        modality="bodyweight",
        api_id=1305
    )
    groin_stretch = Exercise(
        movement_id=9,
        modality="bodyweight",
        api_id=1337
    )
    calves_stretch = Exercise(
        movement_id=10,
        modality="bodyweight",
        api_id=1348
    )
    anterior_deltoid_stretch = Exercise(
        movement_id=11,
        modality="bodyweight",
        api_id=57
    )
    lateral_deltoid_stretch = Exercise(
        movement_id=12,
        modality="bodyweight",
        api_id=1211
    )
    posterior_deltoid_stretch = Exercise(
        movement_id=13,
        modality="bodyweight",
        api_id=1213
    )
    latissimus_dorsi_stretch = Exercise(
        movement_id=14,
        modality="bodyweight",
        api_id=1371
    )
    trapezius_stretch = Exercise(
        movement_id=15,
        modality="bodyweight",
        api_id=1224
    )
    triceps_stretch = Exercise(
        movement_id=16,
        modality="bodyweight",
        api_id=1773
    )
    biceps_stretch = Exercise(
        movement_id=17,
        modality="bodyweight",
        api_id=1217
    )
    rectus_abdominus_stretch = Exercise(
        movement_id=18,
        modality="bodyweight",
        api_id=1249
    )
    obliques_stretch = Exercise(
        movement_id=19,
        modality="bodyweight",
        api_id=1252
    )
    erector_spinae_stretch = Exercise(
        movement_id=20,
        modality="bodyweight",
        api_id=1258
    )
    bb_bench_press = Exercise(
        movement_id=21,
        modality="barbell",
        api_id=563
    )
    db_bench_press = Exercise(
        movement_id=21,
        modality="dumbbell",
        api_id=583
    )
    lv_bench_press = Exercise(
        movement_id=21,
        modality="lever",
        api_id=591
    )
    cb_bench_press = Exercise(
        movement_id=21,
        modality="cable",
        api_id=570
    )
    bb_incline_bench_press = Exercise(
        movement_id=22,
        modality="barbell",
        api_id=543
    )
    db_incline_bench_press = Exercise(
        movement_id=22,
        modality="dumbbell",
        api_id=549
    )
    cb_incline_bench_press = Exercise(
        movement_id=22,
        modality="cable",
        api_id=545
    )
    lv_incline_bench_press = Exercise(
        movement_id=22,
        modality="lever",
        api_id=552
    )
    bb_decline_bench_press = Exercise(
        movement_id=23,
        modality="barbell",
        api_id=556
    )
    db_decline_bench_press = Exercise(
        movement_id=23,
        modality="dumbbell",
        api_id=584
    )
    cb_decline_bench_press = Exercise(
        movement_id=23,
        modality="cable",
        api_id=573
    )
    lv_decline_bench_press = Exercise(
        movement_id=23,
        modality="lever",
        api_id=596
    )
    db_fly = Exercise(
        movement_id=24,
        modality="dumbbell",
        api_id=586
    )
    cb_fly = Exercise(
        movement_id=24,
        modality="cable",
        api_id=575
    )
    lv_fly = Exercise(
        movement_id=24,
        modality="lever",
        api_id=601
    )
    db_incline_fly = Exercise(
        movement_id=25,
        modality="dumbbell",
        api_id=550
    )
    cb_incline_fly = Exercise(
        movement_id=25,
        modality="cable",
        api_id=1488
    )
    lv_incline_fly = Exercise(
        movement_id=25,
        modality="lever",
        api_id=554
    )
    bb_squat = Exercise(
        movement_id=27,
        modality="barbell",
        api_id=996
    )
    db_squat = Exercise(
        movement_id=27,
        modality="dumbbell",
        api_id=847
    )
    lv_squat = Exercise(
        movement_id=27,
        modality="lever",
        api_id=1054
    )
    cb_squat = Exercise(
        movement_id=27,
        modality="cable",
        api_id=834
    )
    bb_deadlift = Exercise(
        movement_id=28,
        modality="barbell",
        api_id=1102
    )
    db_deadlift = Exercise(
        movement_id=28,
        modality="dumbbell",
        api_id=774
    )
    cb_deadlift = Exercise(
        movement_id=28,
        modality="cable",
        api_id=1109
    )
    bb_lunge = Exercise(
        movement_id=29,
        modality="barbell",
        api_id=808
    )
    db_lunge = Exercise(
        movement_id=29,
        modality="dumbbell",
        api_id=840
    )
    lv_leg_curl = Exercise(
        movement_id=30,
        modality="lever",
        api_id=1124
    )
    cb_leg_curl = Exercise(
        movement_id=30,
        modality="cable",
        api_id=1107
    )
    lv_leg_extension = Exercise(
        movement_id=31,
        modality="lever",
        api_id=1049
    )
    lv_calf_raise = Exercise(
        movement_id=32,
        modality="lever",
        api_id=1160
    )
    db_calf_raise = Exercise(
        movement_id=32,
        modality="dumbbell",
        api_id=1148
    )
    bb_calf_raise = Exercise(
        movement_id=32,
        modality="barbell",
        api_id=1143
    )
    cb_calf_raise = Exercise(
        movement_id=32,
        modality="cable",
        api_id=1146
    )
    bb_shoulder_press = Exercise(
        movement_id=33,
        modality="barbell",
        api_id=65
    )
    db_shoulder_press = Exercise(
        movement_id=33,
        modality="dumbbell",
        api_id=73
    )
    lv_shoulder_press = Exercise(
        movement_id=33,
        modality="lever",
        api_id=100
    )
    bb_upright_row = Exercise(
        movement_id=34,
        modality="barbell",
        api_id=102
    )
    db_upright_row = Exercise(
        movement_id=34,
        modality="dumbbell",
        api_id=116
    )
    cb_upright_row = Exercise(
        movement_id=34,
        modality="cable",
        api_id=108
    )
    db_rear_delt_row = Exercise(
        movement_id=35,
        modality="dumbbell",
        api_id=144
    )
    cb_rear_delt_row = Exercise(
        movement_id=35,
        modality="cable",
        api_id=130
    )
    bb_rear_delt_row = Exercise(
        movement_id=35,
        modality="barbell",
        api_id=125
    )
    db_front_lateral_raise = Exercise(
        movement_id=36,
        modality="dumbbell",
        api_id=68
    )
    bb_front_lateral_raise = Exercise(
        movement_id=36,
        modality="barbell",
        api_id=63
    )
    db_side_lateral_raise = Exercise(
        movement_id=37,
        modality="dumbbell",
        api_id=111
    )
    cb_side_lateral_raise = Exercise(
        movement_id=37,
        modality="cable",
        api_id=103
    )
    lv_side_lateral_raise = Exercise(
        movement_id=37,
        modality="lever",
        api_id=120
    )
    db_rear_lateral_raise = Exercise(
        movement_id=38,
        modality="dumbbell",
        api_id=145
    )
    cb_rear_lateral_raise = Exercise(
        movement_id=38,
        modality="cable",
        api_id=132
    )
    lv_chin_up = Exercise(
        movement_id=39,
        modality="lever",
        api_id=508
    )
    cb_chin_up = Exercise(
        movement_id=39,
        modality="cable",
        api_id=496
    )
    bb_row = Exercise(
        movement_id=40,
        modality="barbell",
        api_id=392
    )
    cb_row = Exercise(
        movement_id=40,
        modality="cable",
        api_id=405
    )
    db_row = Exercise(
        movement_id=40,
        modality="dumbbell",
        api_id=414
    )
    lv_row = Exercise(
        movement_id=40,
        modality="lever",
        api_id=422
    )
    cb_pulldown = Exercise(
        movement_id=41,
        modality="cable",
        api_id=471
    )
    lv_pulldown = Exercise(
        movement_id=41,
        modality="lever",
        api_id=488
    )
    bb_pullover = Exercise(
        movement_id=42,
        modality="barbell",
        api_id=462
    )
    db_pullover = Exercise(
        movement_id=42,
        modality="dumbbell",
        api_id=587
    )
    cb_pullover = Exercise(
        movement_id=42,
        modality="cable",
        api_id=465
    )
    lv_pullover = Exercise(
        movement_id=42,
        modality="lever",
        api_id=493
    )
    db_shrug = Exercise(
        movement_id=43,
        modality="dumbbell",
        api_id=517
    )
    bb_shrug = Exercise(
        movement_id=43,
        modality="barbell",
        api_id=512
    )
    cb_shrug = Exercise(
        movement_id=43,
        modality="cable",
        api_id=515
    )
    lv_shrug = Exercise(
        movement_id=43,
        modality="lever",
        api_id=524
    )
    bb_close_grip_press = Exercise(
        movement_id=44,
        modality="barbell",
        api_id=254
    )
    lv_close_grip_press = Exercise(
        movement_id=44,
        modality="lever",
        api_id=293
    )
    bb_curl = Exercise(
        movement_id=45,
        modality="barbell",
        api_id=319
    )
    db_curl = Exercise(
        movement_id=45,
        modality="dumbbell",
        api_id=327
    )
    cb_curl = Exercise(
        movement_id=45,
        modality="cable",
        api_id=322
    )
    lv_curl = Exercise(
        movement_id=45,
        modality="lever",
        api_id=330
    )
    bb_triceps_extension = Exercise(
        movement_id=46,
        modality="barbell",
        api_id=258
    )
    db_triceps_extension = Exercise(
        movement_id=46,
        modality="dumbbell",
        api_id=284
    )
    cb_triceps_extension = Exercise(
        movement_id=46,
        modality="cable",
        api_id=269
    )
    lv_triceps_extension = Exercise(
        movement_id=46,
        modality="lever",
        api_id=300
    )
    bb_preacher_curl = Exercise(
        movement_id=47,
        modality="barbell",
        api_id=331
    )
    db_preacher_curl = Exercise(
        movement_id=47,
        modality="dumbbell",
        api_id=341
    )
    cb_preacher_curl = Exercise(
        movement_id=47,
        modality="cable",
        api_id=337
    )
    lv_preacher_curl = Exercise(
        movement_id=47,
        modality="lever",
        api_id=344
    )
    cb_pushdown = Exercise(
        movement_id=48,
        modality="cable",
        api_id=277
    )
    bb_reverse_curl = Exercise(
        movement_id=49,
        modality="barbell",
        api_id=348
    )
    cb_reverse_curl = Exercise(
        movement_id=49,
        modality="cable",
        api_id=351
    )
    lv_reverse_curl = Exercise(
        movement_id=49,
        modality="lever",
        api_id=355
    )
    bw_sit_up = Exercise(
        movement_id=50,
        modality="bodyweight",
        api_id=693
    )
    bw_twisting_sit_up = Exercise(
        movement_id=51,
        modality="bodyweight",
        api_id=748
    )
    bw_hyperextension = Exercise(
        movement_id=52,
        modality="bodyweight",
        api_id=2032
    )
    bw_front_plank = Exercise(
        movement_id=53,
        modality="bodyweight",
        api_id=700
    )
    bw_rear_plank = Exercise(
        movement_id=54,
        modality="bodyweight",
        api_id=798
    )
    db_thruster = Exercise(
        movement_id=55,
        modality="dumbbell",
        api_id=1656
    )
    bb_thruster = Exercise(
        movement_id=55,
        modality="dumbbell",
        api_id=1613
    )
    bw_burpee = Exercise(
        movement_id=55,
        modality="bodyweight",
        api_id=1
    )
    stairclimber = Exercise(
        movement_id=56,
        modality="stairclimber",
        api_id=1407
    )
    treadmill = Exercise(
        movement_id=56,
        modality="treadmill",
        api_id=1408
    )
    jog = Exercise(
        movement_id=56,
        modality="bodyweight",
        api_id=1909
    )
    exercises = [
        chest_warmup,
        leg_warmup,
        shoulder_warmup,
        back_warmup,
        arm_warmup,
        pectoralis_major_stretch,
        pectoralis_minor_stretch,
        quadriceps_stretch,
        groin_stretch,
        calves_stretch,
        anterior_deltoid_stretch,
        lateral_deltoid_stretch,
        posterior_deltoid_stretch,
        latissimus_dorsi_stretch,
        trapezius_stretch,
        triceps_stretch,
        biceps_stretch,
        rectus_abdominus_stretch,
        obliques_stretch,
        erector_spinae_stretch,
        bb_bench_press,
        db_bench_press,
        lv_bench_press,
        cb_bench_press,
        bb_incline_bench_press,
        db_incline_bench_press,
        cb_incline_bench_press,
        lv_incline_bench_press,
        bb_decline_bench_press,
        db_decline_bench_press,
        cb_decline_bench_press,
        lv_decline_bench_press,
        db_fly,
        cb_fly,
        lv_fly,
        db_incline_fly,
        cb_incline_fly,
        lv_incline_fly,
        bb_squat,
        db_squat,
        lv_squat,
        cb_squat,
        bb_deadlift,
        db_deadlift,
        cb_deadlift,
        bb_lunge,
        db_lunge,
        lv_leg_curl,
        cb_leg_curl,
        lv_leg_extension,
        lv_calf_raise,
        db_calf_raise,
        bb_calf_raise,
        cb_calf_raise,
        bb_shoulder_press,
        db_shoulder_press,
        lv_shoulder_press,
        bb_upright_row,
        db_upright_row,
        cb_upright_row,
        db_rear_delt_row,
        cb_rear_delt_row,
        bb_rear_delt_row,
        db_front_lateral_raise,
        bb_front_lateral_raise,
        db_side_lateral_raise,
        cb_side_lateral_raise,
        lv_side_lateral_raise,
        db_rear_lateral_raise,
        cb_rear_lateral_raise,
        lv_chin_up,
        cb_chin_up,
        bb_row,
        cb_row,
        db_row,
        lv_row,
        cb_pulldown,
        lv_pulldown,
        bb_pullover,
        db_pullover,
        cb_pullover,
        lv_pullover,
        db_shrug,
        bb_shrug,
        cb_shrug,
        lv_shrug,
        bb_close_grip_press,
        lv_close_grip_press,
        bb_curl,
        db_curl,
        cb_curl,
        lv_curl,
        bb_triceps_extension,
        db_triceps_extension,
        cb_triceps_extension,
        lv_triceps_extension,
        bb_preacher_curl,
        db_preacher_curl,
        cb_preacher_curl,
        lv_preacher_curl,
        cb_pushdown,
        bb_reverse_curl,
        cb_reverse_curl,
        lv_reverse_curl,
        bw_sit_up,
        bw_twisting_sit_up,
        bw_hyperextension,
        bw_front_plank,
        bw_rear_plank,
        db_thruster,
        bb_thruster,
        bw_burpee,
        stairclimber,
        treadmill,
        jog
    ]
    for exercise in exercises:
        db.session.add(exercise)
    db.session.commit()


def undo_exercises():
    db.session.execute('TRUNCATE exercises RESTART IDENTITY CASCADE;')
    db.session.commit()
