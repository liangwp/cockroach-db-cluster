#!/bin/bash
rm -rf dbcluster/ca-key dbcluster/certs
docker volume rm \
    roach-db-1-data \
    roach-db-2-data \
    roach-db-3-data \
    roach-db-postgres-data
