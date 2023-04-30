## Set up psycopg

Below link discusses how to setup psycopg anf import in python program:

https://pypi.org/project/psycopg2/

The simplest method is to get the stand-alone package.

pip install psycopg2-binary

## Configure pg_hba.conf

This file is located at C:\Program Files\PostgreSQL\13\data path in Windows machines.

In Linux, the file location is /etc/postgresql/[VERSION]/main/pg_hba.conf

Use the below link for more details:

https://dba.stackexchange.com/questions/83984/connect-to-postgresql-server-fatal-no-pg-hba-conf-entry-for-host

If not configured properly to recieve connections, the below error happens:

port 5432 failed: FATAL: no pg_hba.conf entry for host
