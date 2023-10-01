from yoyo import step

# Using python is more flexible and allows being more explicit intent when
# defining migration scripts.
# https://ollycope.com/software/yoyo/latest/#migrations-as-python-scripts

apply = 'CREATE TABLE bar (id INT, bee VARCHAR(20), PRIMARY KEY (id))'
rollback = 'DROP TABLE bar'

steps = [
    step(apply, rollback)
]
