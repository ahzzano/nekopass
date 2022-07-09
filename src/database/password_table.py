from sqlalchemy import Table, Column, Integer, String
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