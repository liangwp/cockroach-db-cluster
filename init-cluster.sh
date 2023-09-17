#!/bin/bash

sleep 20
# cockroach cert list --certs-dir=/certs
cockroach init --certs-dir=/certs --host=cockroach-db-1.local:26357

if [ $? -eq 1 ]; then
    echo "Cluster already initialised. This is fine"
fi
