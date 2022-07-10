from sqlalchemy import create_engine
from sqlalchemy import text

import src.database.password_table as ptable

engine = create_engine('sqlite+pysqlite:///database.db', future=True)
connection = engine.connect()
password_table = ptable.create_password_table(engine)

def engine_execute_command(command, *args):
    result = connection.execute(text(command), args)
    print(result.all())


def add_password(account_name: str, password: str, nickname: str = ''):
    ptable.insert_to_password_table(password_table, connection, {'account_name': account_name, 'nickname': nickname, 'password': password})

def get_accounts():
    select_command = password_table.select()
    results = connection.execute(select_command)
    return results