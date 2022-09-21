# neverdrains

This is a basic Django recreation of Karl DeAngelo's fantastic DTM software. As of now, this is meant to be a minimal demo app for a Herb-style unlimited qualifying format without any finals formats implemented.

## Run database locally

Use `postgres:14.4` image to match the latest PostgreSQL offering from Azure. For dev, the standard `postgres` user is fine, especially since that user should have permissions to create and tear down the test database. We'll want to create our own user for prod later, which will have no such powers since there won't be a test database in prod.

```
mkdir data
docker run -itd -e POSTGRES_PASSWORD=<PASSWORD> -p 5432:5432 -v $(pwd)/data:/var/lib/postgresql/data --name postgresql postgres:14.4
```

Ensure the `neverdrains` database exists:
```
PGPASSWORD=<PASSWORD> psql -U postgres --host=127.0.0.1
```
