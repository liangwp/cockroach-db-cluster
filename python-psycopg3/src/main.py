print('hello world python')

import psycopg # this is psycopg3
# import psycopg2 as psycopg
import os
import time

dbhost = os.environ['DATABASE_HOST']
dbname = os.environ['DATABASE']
user = os.environ['USER']
pswd = os.environ['PASSWORD']


# Connect to an existing database
with psycopg.connect(f'postgresql://{user}:{pswd}@{dbhost}/{dbname}') as conn:

    print('creating table if necessary')
    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS test_psycopg (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test_psycopg (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

        conn.commit()
    
    with conn.cursor() as cur:
        # Query the database and obtain data as Python objects.
        query = "SELECT * FROM test_psycopg ORDER BY id ASC"

        print(f'cursor.execute: {query}, then get all data from cursor using fetchall()')
        cur.execute(query)
        # We can also use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records at once.
        k = cur.fetchall()
        for idx, record in enumerate(k):
            print(f'{idx}, {record}') # record is (1, 100, "abc'def")

        print(f'cursor.execute: {query}, then iterate using fetchone().')
        cur.execute(query)
        
        while True:
            record = cur.fetchone()
            if record is None:
                break
            print(record)

        print(f'cursor.execute: {query}, then iterate on the cursor')
        cur.execute(query)
        for idx, record in enumerate(cur):
            print(f'{idx}, {record}') # record is (1, 100, "abc'def")

        print(f'cursor.execute: {query}, then iterate using fetchmany()')
        cur.execute(query)
        fetch_size = 3
        while True:
            records = cur.fetchmany(size=fetch_size) # this doesn't seem to do what we expect it to do, maybe a cockroachdb-specific behaviour
            for idx, record in enumerate(records):
                print(f'{idx}, {record}') # record is (1, 100, "abc'def")
            if len(records) < fetch_size:
                break

        print(f'cursor.execute: {query}, then get all data from cursor using fetchall()')
        cur.execute(query)
        # We can also use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records at once.
        k = cur.fetchall()
        for idx, record in enumerate(k):
            print(f'{idx}, {record}') # record is (1, 100, "abc'def")

        # Make the changes to the database persistent
        conn.commit()

print('python done')