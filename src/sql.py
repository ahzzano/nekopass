from sqlalchemy import create_engine
from sqlalchemy import text

import database.password_table as ptable

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)

password_table = ptable.create_password_table(engine)

def engine_execute_command(command, *args):
    with engine.connect() as conn:
        result = conn.execute(text(command), args)
        print(result.all())


ptable.insert_to_password_table(password_table, engine, {'account_name': 'a', 'nickname': 'test', 'password': 'pwrd'})
