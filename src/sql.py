from sqlalchemy import create_engine
from sqlalchemy import text

import database.main_table as mtable

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)

mtable.create_password_table(engine)

def engine_execute_command(command, *args):
    with engine.connect() as conn:
        result = conn.execute(text(command), args)
        print(result.all())

def create_table():
    return