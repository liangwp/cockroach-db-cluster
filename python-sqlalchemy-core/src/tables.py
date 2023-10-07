
from sqlalchemy import Table, Column, Integer, Boolean, String

# Refer to the migration to update the sqlalchemy table.
def reflect_table(engine, metadata_obj, table_name):
    test_table = Table(table_name, metadata_obj, autoload_with=engine)
    return test_table

def manually_set_up_table(engine, metadata_obj, table_name):
    test_table = Table(
        table_name,
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("value", String(30)),
        Column("value2", Integer),
        # Column("new_column", Boolean)
        Column("new_column", Boolean, nullable=False, default=True)
    )
    return test_table
