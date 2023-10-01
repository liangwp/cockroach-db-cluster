# CockroachDB Cluster

Experimental CockroachDB cluster setup in docker.

This is suitable for:

* Local testing and learning
* Bare-metal (offline) deployment

### Features

- [x] Automatically create the cluster.
    * https://www.cockroachlabs.com/docs/stable/deploy-cockroachdb-on-premises
    - [x] Create certs from short-lived container, self-signed certificate for
          local testing
    - [x] Does not create certs unnecessarily
    - [x] Init cluster from short-lived container, safe to init even if cluster
          already exists
- [x] Load balancing across cluster
    - [x] for http console
    - [x] for cockroachdb sql client
- [x] Set up automation for using the cluster with multiple projects
      (assume one project uses one database)
    - [x] Script for creating a database and its user
- [x] Set up postgres for feature comparison with cockroachdb
- [ ] Example nodejs code to use this cluster
    - pg and pg-migrate ?
    - knex.js?
    - https://sqorn.org/benchmarks.html ?
- [ ] Example python code to use this cluster
    - [x] using psycopg3 directly
    - sqlalchemy core and alembic? (alembic is too massive to be useful)
    - sqlalchemy core and yoyo-migrations?

### Prerequisites

Tested on the following:
- Linux ([EndeavourOS](https://endeavouros.com/))
- [docker](https://www.docker.com/get-started/) >= 24.0.5
- docker compose >= 2.20.3

### Quickstart

1. Clone this repository
    - `cd cockroach-db-cluster`: Enter the project root directory.
    - Unless otherwise stated, all commands in documentation are meant to be
      run from this directory.
1. `cp dbcluster/.env.example dbcluster/.env`
    - Edit variables as necessary. Default values in `.env.example` should be
      sufficient to simply run the system.
    - `.env` file should contain deployment-specific values and should not be
      committed to the repository.
1. `docker compose -f dbcluster/docker-compose.yml up`: Sets up a 3-instance
    cluster
    - Create the required certs
    - Create a docker volume for each instance
    - Start the cluster instances
    - Init the cluster (after some healthcheck delays)
    - Set a password for the `root` user
    - Create HAProxy container with bind-mounted configs
1. Using the current configs, cockroachdb console is served by all 3 instances
   through https. Browser will complain about security but that's fine for a
   dev/test cluster.
    - https://localhost:8081
    - https://localhost:8082
    - https://localhost:8083
1. [HAProxy](http://docs.haproxy.org/2.8/intro.html) has been set up to serve
   out the web console as well as sql clients. Only the web console port has
   been forwarded to the host network.
    - https://localhost:8080

### Create Database and User

1. Edit `./dbcluster/scripts/create-db-and-user.sh`, to set the `DATABASE`, `USER`, and
  `PASSWORD`. These must agree with whatever is set in the client apps.
1. If necessary, `chmod +x ./dbcluster/scripts/create-db-and-user.sh`.
1. Run `./dbcluster/scripts/create-db-and-user.sh`.
1. Some other program should be able to use this database, through this user,
   either using a cockroachdb client or a postgres client.

### Run test applications (WIP)

Example code is provided for testing with the cluster, compared with postgres.

#### Postgres DB

For feature/behaviour comparison, the client applications may connect to either
postgres or cockroachdb.

1. `docker compose -f ./dbcluster/docker-compose-postgres.yml up`

#### Python psycopg3 client

1. Edit `./python-psycopg3/docker-compose.yml`, uncomment environment
   variables to choose either cockroachdb or postgres.
1. `docker compose -f ./python-psycopg3/docker-compose.yml up --build`
1. see some logs...
1. `docker compose -f ./python-psycopg3/docker-compose.yml down`

#### More clients WIP


### Stop the Cluster

1. `docker compose -f ./dbcluster/docker-compose.yml down`: Stop the cluster
    - Does not destroy the cluster or its data.
    - Running `docker compose -f ./dbcluster/docker-compose.yml up` again will revive the cluster.
1. `docker compose -f ./dbcluster/docker-compose-postgres.yml down`: Stop postgres

### Clean Up the Entire Cluster

This removes the entire cluster and its data.

1. Stop the cluster (see above).
1. `sudo ./dbcluster/scripts/destroy-cluster.sh`: Remove the certs and docker
   volumes that were created.
