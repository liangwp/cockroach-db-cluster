#!/bin/bash

# This file should be edited to create databases and users in the cluster.
# For simplicity, for now, we create one database per user.

DATABASE=some-db
USER=some-user
PASSWORD=some-pswd

# connect to the loadbalancer instance
INTERNAL_CLUSTER_INSTANCE=cockroach-db.local:26257

# randomly connect to some instance
# INTERNAL_CLUSTER_INSTANCE=cockroach-db-2.local:26257

# # https://www.cockroachlabs.com/docs/stable/cockroach-sql
# docker exec -it $CONTAINER_NAME ./cockroach --host=$HOSTNAME_CLUSTER_INSTANCE \
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
docker compose run --entrypoint "cockroach sql" \
    cluster-init \
    --host=$INTERNAL_CLUSTER_INSTANCE \
    --certs-dir=/certs \
    --execute "CREATE DATABASE IF NOT EXISTS pyserver;" \
    --execute "CREATE USER IF NOT EXISTS pyserver WITH PASSWORD 'pyserver';" \
    --execute "GRANT ALL ON DATABASE pyserver TO pyserver;"