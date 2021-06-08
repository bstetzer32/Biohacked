from app.models import db, Scheme


def seed_schemes():
    compound_1 = Scheme(
        name="Compound 1",
        sets=4,
        reps="18,15,12,15+",
        tempo="4,2,1",
        base_set=2,
        modifier=0.30,
        direction=True
    )
    compound_2 = Scheme(
        name="Compound 2",
        sets=4,
        reps="12,9,6,9+",
        tempo="2,0,2",
        base_set=2,
        modifier=0.15,
        direction=True
    )
    compound_3 = Scheme(
        name="Compound 3",
        sets=4,
        reps="15,12,9,12+",
        tempo="2,0,2",
        base_set=2,
        modifier=0.23,
        direction=True
    )
    isolated_1 = Scheme(
        name="Isolated 1",
        sets=3,
        reps="18,15,18+",
        tempo="4,2,1",
        base_set=1,
        modifier=0.37,
        direction=True
    )
    isolated_2 = Scheme(
        name="Isolated 2",
        sets=3,
        reps="12,9,12+",
        tempo="2,0,2",
        base_set=1,
        modifier=0.23,
        direction=True
    )
    isolated_3 = Scheme(
        name="Isolated 3",
        sets=3,
        reps="15,12,15+",
        tempo="2,0,2",
        base_set=1,
        modifier=0.30,
        direction=True
    )
    core_dynamic = Scheme(
        name="Core Dynamic",
        sets=3,
        reps="20",
        tempo="1,0,1"
    )
    core_static = Scheme(
        name="Core Static",
        sets=3,
        time=60
    )
    stretch = Scheme(
        name="stretch",
        sets=3,
        time=30
    )
    warmup = Scheme(
        name="Warmup",
        sets=2,
        reps="10",
        tempo="4,2,1"
    )
    tabata_1 = Scheme(
        name="TABATA 1",
        sets=8,
        tempo="20,10"
    )
    tabata_2 = Scheme(
        name="TABATA 2",
        sets=12,
        tempo="20,10"
    )
    tabata_3 = Scheme(
        name="TABATA 3",
        sets=16,
        tempo="20,10"
    )
    cooldown = Scheme(
        name="Cooldown",
        sets=1,
        time=600
    )
    schemes = [compound_1,
               compound_2,
               compound_3,
               isolated_1,
               isolated_2,
               isolated_3,
               core_dynamic,
               core_static,
               stretch,
               warmup,
               tabata_1,
               tabata_2,
               tabata_3,
               cooldown]
    for scheme in schemes:
        db.session.add(scheme)
    db.session.commit()


def undo_schemes():
    db.session.execute('TRUNCATE schemes RESTART IDENTITY CASCADE;')
    db.session.commit()
