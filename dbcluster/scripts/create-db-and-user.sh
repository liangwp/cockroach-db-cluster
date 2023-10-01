#!/bin/bash

# This file should be edited to create databases and users in the cluster.
# For simplicity, for now, we create one database per user.

# hyphens not allowed in database or user name
DB_NAME=test_app
DB_USER=test_app_user
DB_PSWD=test_app_pswd

# connect to the loadbalancer instance
COCKROACH_HOST=cockroach-db.local:26257

# randomly connect to some instance
# COCKROACH_HOST=cockroach-db-2.local:26257

# # https://www.cockroachlabs.com/docs/stable/cockroach-sql
# docker exec -it $CONTAINER_NAME ./cockroach --host=$COCKROACH_HOST \
#     --user=root --certs-dir=/certs sql 

# docker compose --entrypoint ./cockroach sql \
#     --host=cockroach-db-2.local:26257 \
#     --certs-dir=/certs --execute "SELECT * FROM defaultdb;"

# # get into a terminal in container
# docker compose run --entrypoint "/bin/bash" cluster-init
# # get into a sql shell when in terminal in container
# ./cockroach sql --host=cockroach-db-2.local:26257 --certs-dir=/certs

# # get straight into sql shell
# docker compose run --entrypoint "cockroach sql" cluster-init --host=cockroach-db-2.local:26257 --certs-dir=/certs

# run a command directly
docker compose -f ./dbcluster/docker-compose.yml \
    run --no-deps --entrypoint "cockroach sql" \
    cluster-init \
    --host=$COCKROACH_HOST \
    --certs-dir=/certs \
    --execute "CREATE DATABASE IF NOT EXISTS $DB_NAME;" \
    --execute "CREATE USER IF NOT EXISTS $DB_USER WITH PASSWORD '$DB_PSWD';" \
    --execute "GRANT ALL ON DATABASE $DB_NAME TO $DB_USER;"

# docker login using the new user, and run some commands:
# docker compose run --entrypoint "cockroach sql" cluster-init --host=cockroach-db.local:26257 --certs-dir=/certs --user=some_user --database=some_db
# > CREATE TABLE pyserver_test (id INT PRIMARY KEY, name STRING);
# > INSERT INTO pyserver_test (id, name) VALUES (1, 'frog');
# > SELECT * FROM pyserver_test;
# > DROP TABLE pyserver_test;
