from yoyo import step

# Using python is more flexible and allows being more explicit intent when
# defining migration scripts.
# https://ollycope.com/software/yoyo/latest/#migrations-as-python-scripts

apply = 'CREATE TABLE test_sqlalchemy (id INT, value VARCHAR(20), value2 INT, PRIMARY KEY (id))'
rollback = 'DROP TABLE test_sqlalchemy'

steps = [
    step(apply, rollback)
]
