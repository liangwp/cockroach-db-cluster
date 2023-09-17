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
- [ ] Load balancing across cluster
    - [ ] for http console
    - [ ] for sql clients
- [ ] Set up automation for using the cluster with multiple projects
      (assume one project uses one database)
    - [ ] Script for creating a database and its user

### Prerequisites

Tested on the following:
- Linux ([EndeavourOS](https://endeavouros.com/))
- [docker](https://www.docker.com/get-started/) >= 24.0.5
- docker compose >= 2.20.3

### Quickstart

1. Clone this repository
    - `cd cockroach-db-cluster`: enter the project root directory.
    - Unless otherwise stated, all commands in documentation are meant to be
      run from this directory.
1. `cp .env.example .env`
    - Edit variables as necessary. Default values in `.env.example` should be
      sufficient to simply run the system.
    - `.env` file should contain deployment-specific values and should not be
      committed to the repository.
1. `docker compose up`: Sets up a 3-instance cluster
    - Create the required certs
    - Create a docker volume for each instance
    - Start the cluster instances
    - Init the cluster
    - Set a password for the `root` user
1. Using the current configs, cockroachdb console is served by all 3 instances
   through https. Browser will complain about security but that's fine for a
   dev/test cluster.
    - https://localhost:8081
    - https://localhost:8082
    - https://localhost:8083
1. `docker compose down`: Stop the cluster
    - Running `docker compose up` again will revive the cluster.
1. `sudo ./cleanup.sh`: Remove the certs and docker volumes that were
   created.
