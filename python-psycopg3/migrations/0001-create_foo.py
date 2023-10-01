from yoyo import step

__depends__ = {"0000-initial_schema"}

apply = "CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id))"
rollback = "DROP TABLE foo"

steps = [
    step(apply, rollback)
]