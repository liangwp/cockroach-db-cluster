from yoyo import step

__depends__ = {"0001-create_foo"}

apply = 'ALTER TABLE foo ADD COLUMN baz INT NOT NULL'

steps = [
    step(apply)
]