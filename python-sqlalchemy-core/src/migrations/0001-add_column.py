from yoyo import step

__depends__ = {"0000-initial_schema"}

apply = 'ALTER TABLE test_sqlalchemy ADD COLUMN new_column BOOLEAN NOT NULL DEFAULT TRUE'
rollback = 'ALTER TABLE test_sqlalchemy DROP COLUMN new_column'

steps = [
    step(apply, rollback)
]