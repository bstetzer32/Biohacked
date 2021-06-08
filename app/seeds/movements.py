from app.models import db, Movement


def seed_movements():
    chest_warmup = Movement(
        name="Chest Warmup",
        muscle_group="Chest",
        type="warmup"
    )
    leg_warmup = Movement(
        name="Leg Warmup",
        muscle_group="Legs",
        type="warmup"
    )
    shoulders_warmup = Movement(
        name="Shoulder Warmup",
        muscle_group="Shoulders",
        type="warmup"
    )
    back_warmup = Movement(
        name="Back Warmup",
        muscle_group="Back",
        type="warmup"
    )
    arms_warmup = Movement(
        name="Arm Warmup",
        muscle_group="Arms",
        type="warmup"
    )
    pectoralis_major_stretch = Movement(
        name="Pectoralis Major Stretch",
        muscle_group="Chest",
        type="stretch"
    )
    pectoralis_minor_stretch = Movement(
        name="Pectoralis Minor Stretch",
        muscle_group="Chest",
        type="stretch"
    )
    quadriceps_stretch = Movement(
        name="Quadriceps Stretch",
        muscle_group="Legs",
        type="stretch"
    )
    groin_stretch = Movement(
        name="Groin Stretch",
        muscle_group="Legs",
        type="stretch"
    )
    calves_stretch = Movement(
        name="Calves Stretch",
        muscle_group="Legs",
        type="stretch"
    )
    anterior_deltoid_stretch = Movement(
        name="Anterior Deltoid Stretch",
        muscle_group="Shoulders",
        type="stretch"
    )
    lateral_deltoid_stretch = Movement(
        name="Lateral Deltoid Stretch",
        muscle_group="Shoulders",
        type="stretch"
    )
    posterior_deltoid_stretch = Movement(
        name="Posterior Deltoid Stretch",
        muscle_group="Shoulders",
        type="stretch"
    )
    latissimus_dorsi_stretch = Movement(
        name="Latissimus Dorsi Stretch",
        muscle_group="Back",
        type="stretch"
    )
    trapezius_stretch = Movement(
        name="Trapezius Stretch",
        muscle_group="Back",
        type="stretch"
    )
    triceps_stretch = Movement(
        name="Triceps Stretch",
        muscle_group="Arms",
        type="stretch"
    )
    biceps_stretch = Movement(
        name="Biceps Stretch",
        muscle_group="Arms",
        type="stretch"
    )
    rectus_abdominus_stretch = Movement(
        name="Rectus Abdominus Stretch",
        muscle_group="Abdominals",
        type="stretch"
    )
    obliques_stretch = Movement(
        name="Obliques Stretch",
        muscle_group="Abdominals",
        type="stretch"
    )
    erector_spinae_stretch = Movement(
        name="Erector Spinae Stretch",
        muscle_group="Abdominals",
        type="stretch"
    )
    bench_press = Movement(
        name="Bench Press",
        muscle_group="Chest",
        type="compound"
    )
    incline_bench_press = Movement(
        name="Incline Bench Press",
        muscle_group="Chest",
        type="compound"
    )
    decline_bench_press = Movement(
        name="Decline Bench Press",
        muscle_group="Chest",
        type="compound"
    )
    fly = Movement(
        name="Fly",
        muscle_group="Chest",
        type="isolated"
    )
    incline_fly = Movement(
        name="Incline Fly",
        muscle_group="Chest",
        type="isolated"
    )
    decline_fly = Movement(
        name="Decline Fly",
        muscle_group="Chest",
        type="isolated"
    )
    squat = Movement(
        name="Squat",
        muscle_group="Legs",
        type="compound"
    )
    deadlift = Movement(
        name="Deadlift",
        muscle_group="Legs",
        type="compound"
    )
    lunge = Movement(
        name="Lunge",
        muscle_group="Legs",
        type="compound"
    )
    leg_curl = Movement(
        name="Leg Curl",
        muscle_group="Legs",
        type="isolated"
    )
    leg_extension = Movement(
        name="Leg Extension",
        muscle_group="Legs",
        type="isolated"
    )
    calf_raise = Movement(
        name="Calf Raise",
        muscle_group="Legs",
        type="isolated"
    )
    shoulder_press = Movement(
        name="Shoulder Press",
        muscle_group="Shoulders",
        type="compound"
    )
    upright_row = Movement(
        name="Upright Row",
        muscle_group="Shoulders",
        type="compound"
    )
    rear_delt_row = Movement(
        name="Rear Delt Row",
        muscle_group="Shoulders",
        type="compound"
    )
    front_lateral_raise = Movement(
        name="Front Lateral Raise",
        muscle_group="Shoulders",
        type="isolated"
    )
    side_lateral_raise = Movement(
        name="Side Lateral Raise",
        muscle_group="Shoulders",
        type="isolated"
    )
    rear_lateral_raise = Movement(
        name="Rear Lateral Raise",
        muscle_group="Shoulders",
        type="isolated"
    )
    chin_up = Movement(
        name="Chin-up",
        muscle_group="Back",
        type="compound"
    )
    row = Movement(
        name="Row",
        muscle_group="Back",
        type="compound"
    )
    pulldown = Movement(
        name="Pulldown",
        muscle_group="Back",
        type="compound"
    )
    pullover = Movement(
        name="Pullover",
        muscle_group="Back",
        type="isolated"
    )
    shrug = Movement(
        name="Shrug",
        muscle_group="Back",
        type="isolated"
    )
    close_grip_press = Movement(
        name="Close Grip Press",
        muscle_group="Arms",
        type="compound"
    )
    curl = Movement(
        name="Curl",
        muscle_group="Arms",
        type="isolated"
    )
    triceps_extension = Movement(
        name="Triceps Extension",
        muscle_group="Arms",
        type="isolated"
    )
    preacher_curl = Movement(
        name="Preacher Curl",
        muscle_group="Arms",
        type="isolated"
    )
    pushdown = Movement(
        name="Pushdown",
        muscle_group="Arms",
        type="isolated"
    )
    reverse_curl = Movement(
        name="Reverse Curl",
        muscle_group="Arms",
        type="isolated"
    )
    sit_up = Movement(
        name="Sit Up",
        muscle_group="Abdominals",
        type="compound"
    )
    twisting_sit_up = Movement(
        name="Twisting Sit Up",
        muscle_group="Abdominals",
        type="compound"
    )
    hyperextension = Movement(
        name="Hyperextension",
        muscle_group="Abdominals",
        type="compound"
    )
    front_plank = Movement(
        name="Front Plank",
        muscle_group="Abdominals",
        type="isolated"
    )
    rear_plank = Movement(
        name="Rear Plank",
        muscle_group="Abdominals",
        type="isolated"
    )
    high_intensity_interval_training = Movement(
        name="High Intensity Interval Training",
        muscle_group="Cardiovascular",
        type="cardio"
    )
    cooldown = Movement(
        name="Cooldown",
        muscle_group="Cardiovascular",
        type="cardio"
    )
    movements = [
        chest_warmup,
        leg_warmup,
        shoulders_warmup,
        back_warmup,
        arms_warmup,
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
        bench_press,
        incline_bench_press,
        decline_bench_press,
        fly,
        incline_fly,
        decline_fly,
        squat,
        deadlift,
        lunge,
        leg_curl,
        leg_extension,
        calf_raise,
        shoulder_press,
        upright_row,
        rear_delt_row,
        front_lateral_raise,
        side_lateral_raise,
        rear_lateral_raise,
        chin_up,
        row,
        pulldown,
        pullover,
        shrug,
        close_grip_press,
        curl,
        triceps_extension,
        preacher_curl,
        pushdown,
        reverse_curl,
        sit_up,
        twisting_sit_up,
        hyperextension,
        front_plank,
        rear_plank,
        high_intensity_interval_training,
        cooldown
    ]

    for movement in movements:
        db.session.add(movement)

    db.session.commit()


def undo_movements():
    db.session.execute('TRUNCATE movements RESTART IDENTITY CASCADE;')
    db.session.commit()
