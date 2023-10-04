from yoyo import step

# Using python is more flexible and allows being more explicit intent when
# defining migration scripts.
# https://ollycope.com/software/yoyo/latest/#migrations-as-python-scripts

apply = 'CREATE TABLE test_sqlalchemy (id SERIAL PRIMARY KEY, value VARCHAR(20), value2 INT)'
rollback = 'DROP TABLE test_sqlalchemy'

steps = [
    step(apply, rollback)
]
