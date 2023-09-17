#!/bin/bash
rm -rf ca-key certs
rm -rf node-*-certs
docker volume rm roach-db-1-data roach-db-2-data roach-db-3-data
