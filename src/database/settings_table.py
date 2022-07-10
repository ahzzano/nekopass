from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import insert

def create_settings_table(engine) -> Table:
    metadata_obj = MetaData()

    settings_table = Table(
        "settings",
        metadata_obj,
        Column('property', String(50), primary_key=True),
        Column('value', String(50))
    )

    metadata_obj.create_all(engine)
    return settings_table