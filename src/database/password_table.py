from sqlalchemy import Table, Column, Integer, String, insert
from sqlalchemy import MetaData

def create_password_table(engine):
    metadata_obj = MetaData()

    password_table = Table(
        "passwords",
        metadata_obj,
        Column('account_name', String(50), primary_key=True),
        Column('nickname', String(50)),
        Column('password', String(50))
    )

    metadata_obj.create_all(engine)

    return password_table

def insert_to_password_table(table: Table, engine, data: dict):
    insert_command = table.insert().values(account_name = data['account_name'], nickname = data['nickname'], password = data['password'])

    with engine.connect() as conn:
        conn.execute(insert_command)