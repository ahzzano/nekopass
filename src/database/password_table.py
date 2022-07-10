from importlib.metadata import metadata
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import insert

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

def insert_to_password_table(table: Table, connection, data: dict):
    insert_command = insert(table).values(account_name = data['account_name'], nickname = data['nickname'], password = data['password'])
    connection.execute(insert_command)
    connection.commit()