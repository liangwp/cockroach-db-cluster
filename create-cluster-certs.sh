#!/bin/bash

if [ ! -f "/certs/ca.crt" ]; then
    echo "Creating certificate authority and root cert..."
    cockroach cert create-ca --certs-dir=/certs --ca-key=/ca-key/ca.key
    # creates 1 more file:
    # /certs/ca.crt
else
    echo "Root authority already exists..."
fi

if [ ! -f "/certs/node-1.crt" ]; then
    echo "Creating Node 1 cert..."
    cockroach cert create-node cockroach-db-1.local localhost 127.0.0.1 --certs-dir=/certs --ca-key=/ca-key/ca.key
    cp /certs/ca.crt /node-1-certs/
    mv /certs/node.crt /node-1-certs/
    mv /certs/node.key /node-1-certs/
else
    echo "Node 1 cert already exists..."
fi

if [ ! -f "/certs/node-2.crt" ]; then
    echo "Creating Node 2 cert..."
    cockroach cert create-node cockroach-db-2.local localhost 127.0.0.1 --certs-dir=/certs --ca-key=/ca-key/ca.key
    cp /certs/ca.crt /node-2-certs/
    mv /certs/node.crt /node-2-certs/
    mv /certs/node.key /node-2-certs/
else
    echo "Node 2 cert already exists..."
fi

if [ ! -f "/certs/node-3.crt" ]; then
    echo "Creating Node 3 cert..."
    cockroach cert create-node cockroach-db-3.local localhost 127.0.0.1 --certs-dir=/certs --ca-key=/ca-key/ca.key
    cp /certs/ca.crt /node-3-certs/
    mv /certs/node.crt /node-3-certs/
    mv /certs/node.key /node-3-certs/
else
    echo "Node 3 cert already exists..."
fi

if [ ! -f "/certs/client.root.crt" ]; then
    echo "Creating root client cert..."
    cockroach cert create-client root --certs-dir=/certs --ca-key=/ca-key/ca.key
    # creates 2 files:
    # /certs/client.root.crt
    # /certs/client.root.key
else
    echo "Root client cert already exists..."
fi
