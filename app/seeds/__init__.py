from flask.cli import AppGroup
from .users import seed_users, undo_users
from .movements import seed_movements, undo_movements
from .schemes import seed_schemes, undo_schemes
from .exercises import seed_exercises, undo_exercises

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_movements()
    seed_schemes()
    seed_exercises()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_movements()
    undo_schemes()
    undo_exercises()
    # Add other undo functions here
