#!/bin/bash

sleep 20
# cockroach cert list --certs-dir=/certs
cockroach init --certs-dir=/certs --host=cockroach-db-1.local:26357

if [ $? -eq 1 ]; then
    echo "Cluster already initialised. This is fine"
fi

# https://www.cockroachlabs.com/docs/stable/create-user
echo "Setting root user password..."
./cockroach --host=cockroach-db-2.local:26257 --user=root --certs-dir=/certs --database defaultdb sql --execute="ALTER USER root WITH PASSWORD '$ROOT_PASSWORD';"
