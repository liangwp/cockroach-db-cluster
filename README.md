# CockroachDB Cluster

Experimental CockroachDB cluster setup in docker.

This is suitable for:

* Local testing and learning
* Bare-metal deployment

Considerations:

1. multiple instances / containers
1. security
1. user creation
1. database administration for multiple users / projects

TODO:

- [x] Set up something to create the cluster automatically.
    * https://www.cockroachlabs.com/docs/stable/deploy-cockroachdb-on-premises
- [x] With proper security
- [ ] Should not create certs and init cluster unless necessary
- [ ] With load balancing
- [ ] Some automated way to create databases (for multiple projects)
- [ ] And the users with the right privileges to access the respective databases.


Quickstart:

1. `docker compose up`:
    - create the certs
    - start the cluster instances
    - and init the cluster
    
1. `sudo ./cleanup.sh`: Remove the various host-level directories that were
   created by `docker compose up`.

