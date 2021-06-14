"""reset database

Revision ID: 4efa5886296d
Revises: 
Create Date: 2021-06-11 20:00:51.642276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4efa5886296d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('muscle_group', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('schemes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=True),
    sa.Column('reps', sa.String(length=50), nullable=True),
    sa.Column('tempo', sa.String(length=50), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('rest', sa.Integer(), nullable=True),
    sa.Column('base_set', sa.Integer(), nullable=True),
    sa.Column('modifier', sa.Float(), nullable=True),
    sa.Column('direction', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movement_id', sa.Integer(), nullable=False),
    sa.Column('modality', sa.String(length=50), nullable=False),
    sa.Column('api_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movement_id'], ['movements.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_id')
    )
    op.create_table('questionnaires',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('parq1', sa.String(length=3), nullable=False),
    sa.Column('parq2', sa.String(length=3), nullable=False),
    sa.Column('parq3', sa.String(length=3), nullable=False),
    sa.Column('parq4', sa.String(length=3), nullable=False),
    sa.Column('parq5', sa.String(length=3), nullable=False),
    sa.Column('parq6', sa.String(length=3), nullable=False),
    sa.Column('parq7', sa.String(length=3), nullable=False),
    sa.Column('barbell', sa.String(length=10), nullable=False),
    sa.Column('dumbbell', sa.String(length=10), nullable=False),
    sa.Column('cable', sa.String(length=10), nullable=False),
    sa.Column('lever', sa.String(length=10), nullable=False),
    sa.Column('goal', sa.String(length=8), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('questionnaire_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['questionnaire_id'], ['questionnaires.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routine_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('routine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('routine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workout_exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('max', sa.Float(), nullable=False),
    sa.Column('scheme_id', sa.Integer(), nullable=True),
    sa.Column('workout_id', sa.Integer(), nullable=True),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['scheme_id'], ['schemes.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workout_exercise_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('set', sa.Integer(), nullable=True),
    sa.Column('reps', sa.Integer(), nullable=True),
    sa.Column('load', sa.Integer(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('rest', sa.Integer(), nullable=True),
    sa.Column('routine_result_id', sa.Integer(), nullable=True),
    sa.Column('workout_exercise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['routine_result_id'], ['routine_results.id'], ),
    sa.ForeignKeyConstraint(['workout_exercise_id'], ['workout_exercises.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workout_exercise_results')
    op.drop_table('workout_exercises')
    op.drop_table('workouts')
    op.drop_table('routine_results')
    op.drop_table('routines')
    op.drop_table('questionnaires')
    op.drop_table('exercises')
    op.drop_table('users')
    op.drop_table('schemes')
    op.drop_table('movements')
    # ### end Alembic commands ###
