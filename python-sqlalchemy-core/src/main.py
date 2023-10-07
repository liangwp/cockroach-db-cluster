from yoyo import read_migrations
from yoyo import get_backend

from sqlalchemy import create_engine
from sqlalchemy import text

import os
import asyncio
import random

from sqlalchemy import MetaData
from tables import reflect_table, manually_set_up_table

# WIP: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

async def async_main():
    while True:
        print('hello world')
        await asyncio.sleep(2)

def synchronous_db_calls(connection_string):

    # https://docs.sqlalchemy.org/en/20/core/engines.html#engine-configuration
    engine = create_engine(
        connection_string,
        echo=True,
        echo_pool=True,
        # isolation_level='READ COMMITTED', # postgres default
        pool_size=5,    # default 5
        max_overflow=10, # default 10
    )

    # retrieve (and return) a connection from the pool using context manager
    # implicit transaction, "commit as you go" within the transaction.
    with engine.connect() as conn:
        result = conn.execute(text(
            "INSERT INTO test_sqlalchemy (value, value2, new_column) "
            "VALUES ('abcd', 123, TRUE)"
        ))
        # result.close()
        # print(result.all()) # insert returns no result, will throw an error
        conn.commit() # explicit commit, or it will rollback

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM test_sqlalchemy"))
        # result.close()
        print(result.all()) # select query returns at least an empty list. will not throw
        # conn.commit()
        # will auto rollback if no conn.commit(). no difference for SELECT query.

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    with engine.begin() as conn:
        result = conn.execute(
            text(
                "INSERT INTO test_sqlalchemy (value, value2) "
                "VALUES ('begin', :num)"
            ),
            [{ "num": num1 }, { "num": num2 }] # parameter substitution, 2 rows
        )
        # implicit transaction and commit using engine.begin()

    # try reflecting a table
    metadata_obj = MetaData()
    test_table = reflect_table(engine, metadata_obj, 'test_sqlalchemy')
    print(f'Reflected table:')
    for col in test_table.c.values():
        print(f'--- {col=}')
    print()

    # try setting up the table manually
    metadata_obj_2 = MetaData()
    test_table2 = manually_set_up_table(engine, metadata_obj_2, 'test_sqlalchemy')
    print(f'Manual table (ends up different from reflecting):')
    for col in test_table2.c.values():
        print(f'--- {col=}')
    print()

    # TODO: write into the table using both variants. Maybe both should work...

    engine.dispose()

def main():

    DB_USER = os.environ['DB_USER']
    DB_PSWD = os.environ['DB_PSWD']
    DB_HOST = os.environ['DB_HOST']
    DB_NAME = os.environ['DB_NAME']
    sqlalchemy_connection_string = f'cockroachdb://{DB_USER}:{DB_PSWD}@{DB_HOST}/{DB_NAME}'
    yoyo_connection_string = f'postgresql+psycopg://{DB_USER}:{DB_PSWD}@{DB_HOST}/{DB_NAME}'

    perform_migration(yoyo_connection_string)

    synchronous_db_calls(sqlalchemy_connection_string)

    asyncio.run(async_main())

def perform_migration(connection_string):
    
    print('starting migrations')

    backend = get_backend(connection_string)
    migrations = read_migrations('/workspace/src/migrations')

    with backend.lock():

        # Apply any outstanding migrations
        backend.apply_migrations(backend.to_apply(migrations))

        # Rollback all migrations
        # backend.rollback_migrations(backend.to_rollback(migrations))

    print('migrations done')

if __name__ == '__main__':

    main()
