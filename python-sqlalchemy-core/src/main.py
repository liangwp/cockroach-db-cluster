from yoyo import read_migrations
from yoyo import get_backend

import os
import asyncio

async def async_main():
    while True:
        print('hello world')
        await asyncio.sleep(2)

def main():
    asyncio.run(async_main())

if __name__ == '__main__':

    DB_USER = os.environ['DB_USER']
    DB_PSWD = os.environ['DB_PSWD']
    DB_HOST = os.environ['DB_HOST']
    DB_NAME = os.environ['DB_NAME']

    backend = get_backend(f'postgresql+psycopg://{DB_USER}:{DB_PSWD}@{DB_HOST}/{DB_NAME}')
    migrations = read_migrations('/workspace/src/migrations')

    with backend.lock():

        # Apply any outstanding migrations
        backend.apply_migrations(backend.to_apply(migrations))

        # Rollback all migrations
        # backend.rollback_migrations(backend.to_rollback(migrations))

    main()
