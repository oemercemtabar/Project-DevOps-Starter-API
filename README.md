# Project-DevOps-Starter-API

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
---

## Run

```bash
uvicorn main:app --reload
```

---
## RoadMap

### Day 1 checklist (DevOps mindset, app architecture, local environment)
Today’s key message is: **A service is not only code. A service is code + process + config + dependencies + runtime behavior.**

The checklist:

- [x] created `devops-starter-api`
- [x] created and activated `.venv`
- [x] installed `fastapi` and `uvicorn`
- [x] created `main.py`
- [x] ran app with `uvicorn`
- [x] opened `/docs`
- [x] tested `/health`
- [x] tested `GET /tasks`
- [x] tested `POST /tasks`
- [x] tested `PATCH /tasks/{id}/done`
- [x] generated `requirements.txt`
- [x] wrote basic `README.md`

---

### Day 2 checklist (Linux/processes/ports)

Today’s key messages are:
- A process is a running program on the machine.
- A port is a logical network entry point (door) used by a process on the machine.
- `127.0.0.1` means the local machine itself. It is often also referred to as `localhost`, which usually resolves to the same IP address.
- “Connection refused” usually means no process is listening on that port.
- “Address already in use” usually means another process is already listening on that port.

The checklist:

- [x] started app on port `8000`
- [x] tested `/health`
- [x] ran `lsof -i :8000`
- [x] ran `ps aux | grep uvicorn`
- [x] restarted app on port `8001`
- [x] confirmed `8001` works
- [x] confirmed `8000` no longer works
- [x] tested both `localhost` and `127.0.0.1`

---

### Day 3 checklist (HTTP, APIs, curl, status codes)

Today’s key message is:
- **When debugging an API, always identify the method, path, payload, and resulting status code.**

The checklist:

- [x] updated `main.py` with better status handling
- [x] tested `GET /health` with `curl -i`
- [x] tested `GET /tasks` with `curl -i`
- [x] tested valid `POST /tasks`
- [x] tested invalid `POST /tasks`
- [x] tested wrong path
- [x] tested wrong method
- [x] tested missing task update

---

### Day 4 checklist (Environment variables, configuration, secrets basics)

Today’s key messages are:
- **The same code can behave differently depending on runtime configuration**
- Configuration is how an application runs in a specific environment.
- Hardcoding runtime values makes applications less flexible and less secure.
- Environment variables allow runtime configuration without changing the code.
- `.env` files are useful for local development.
- Secrets are sensitive configuration values and should not be committed to Git.
- `.env.example` documents expected variables safely.

The checklist:

- [x] installed `pydantic-settings`
- [x] created `settings.py`
- [x] updated `main.py` to use settings
- [x] created `.env`
- [x] tested config values through `/`
- [x] tested config values through `/health`
- [x] changed `.env` values and verified runtime change
- [x] tested shell-based env var override
- [x] created `.gitignore`
- [x] created `.env.example`
- [x] regenerated `requirements.txt`

---
### Day 5 checklist (Networking basics, localhost, DNS, reverse proxy concepts)

Today’s key messages are:
- **A service can be running correctly and still be unreachable if it is bound to the wrong interface or accessed through the wrong network path.**
- A running app must not only exist as a process, but also listen on the correct host and port.
- `127.0.0.1` means the loopback interface of the local machine.
- `0.0.0.0` means the server listens on all available network interfaces.
- `0.0.0.0` is mainly a binding address, not the normal address a client browses to.
- DNS translates hostnames into IP addresses.
- A reverse proxy sits in front of an application and forwards requests to it.

The checklist:

- [x] ran Uvicorn with `--host 127.0.0.1`
- [x] tested access through `127.0.0.1`
- [x] tested access through `localhost`
- [x] ran Uvicorn with `--host 0.0.0.0`
- [x] tested access again through `127.0.0.1`
- [x] tested access again through `localhost`
- [x] inspected the listening process with `lsof -i :8000`
- [x] found the local machine IP
- [x] wrote notes about DNS and reverse proxy concepts

--- 

### Day 6 checklist (Logs, debugging basics, failure analysis)

Today’s key messages are:
- Logs are one of the first sources of truth when debugging a system.
- A request reaching the app does not necessarily mean the request succeeded.
- Startup failures, network failures, validation failures, and runtime exceptions are different categories of problems.
- A `500` usually means the server code crashed during request handling.
- Framework logs and application logs provide different kinds of useful information.

The checklist:

- [x] observed normal startup logs
- [x] observed request logs for successful requests
- [x] observed `422` validation failure in logs
- [x] observed `404` path failure in logs
- [x] reproduced a syntax error and read the startup failure
- [x] reproduced an import error and read the startup failure
- [x] reproduced a runtime exception and observed a `500`
- [x] added custom application logging
- [x] observed custom logs from endpoints

---

### Day 7 checklist (Introduction to containers and Docker)

Today’s key messages are:
- **A Docker image defines how the app should run; a container is the running process environment created from that definition.**
- Docker packages an application and its runtime into a reproducible image.
- An image is a build artifact; a container is a running instance of that image.
- A container is still an isolated process environment.
- The application inside the container must listen on `0.0.0.0` to be reachable through published ports.
- Port publishing with `-p host_port:container_port` maps a host port to a container port.


The checklist:
- [x] created `Dockerfile`
- [x] created `.dockerignore`
- [x] built image `devops-starter-api:day7`
- [x] ran container on port `8000`
- [x] tested `/`
- [x] tested `/health`
- [x] tested `/tasks`
- [x] inspected running container with `docker ps`
- [x] ran container with alternate host port mapping

--- 
### Day 8 checklist (Docker images, layers, caching, and build behavior)

Today’s key messages are:
- Docker images are built step by step from Dockerfile instructions.
- Image layers allow Docker to reuse previous build work through caching.
- Dockerfile instruction order affects build speed and cache efficiency.
- `COPY requirements.txt` before `COPY . .` helps avoid unnecessary dependency reinstalls.
- `.dockerignore` reduces build context size and avoids copying unnecessary or sensitive files.

The checklist:

- [x] rebuilt image and observed cache behavior
- [x] rebuilt image again without changes
- [x] changed application code and observed selective rebuild
- [x] explained why dependency copy order matters
- [x] explained why `.dockerignore` matters
- [x] ran `devops-starter-api:day8`
- [x] verified the containerized app still works
- [x] summarized what changed between the first and second rebuilds

---

### Day 9 checklist (Container networking and ports in practice)

Today’s key messages are:
- A running container is not automatically reachable from the host.
- The application inside the container listens on a container port.
- Docker publishes that port to the host with `-p host_port:container_port`.
- `EXPOSE` documents the intended container port, but does not publish it to the host.
- Correct app binding inside the container and correct port publishing are both required for reachability.

The checklist:

- [x] ran container with `-p 8000:8000`
- [x] tested `/health` on host port `8000`
- [x] ran container with `-p 8001:8000`
- [x] tested `/health` on host port `8001`
- [x] confirmed wrong host port fails
- [x] inspected `docker ps` port mappings
- [x] ran container without `-p`
- [x] confirmed host access fails without published port
- [x] ran container in detached mode
- [x] inspected logs with `docker logs`

--- 
### Day 10 checklist (Dockerfile improvements, image hygiene, and first production-minded refinements)

Today’s key messages are:
- **A good container image is not just something that starts — it should also be clean, predictable, and suited for runtime use.**
- A Dockerfile should not only work, but also be intentional and clean.
- Python runtime environment variables like `PYTHONUNBUFFERED=1` improve log behavior in containers.
- `.dockerignore` is part of both build performance and image hygiene.
- A runtime container should avoid unnecessary local-development behavior such as automatic reload.
- Cleaner images make later deployment and debugging easier.

The checklist:

- [x] updated Dockerfile with Python environment settings
- [x] improved `.dockerignore`
- [x] built image `devops-starter-api:day10`
- [x] ran container on port `8000`
- [x] tested `/`
- [x] tested `/health`
- [x] tested `/tasks`
- [x] observed logs from the running container
- [x] explained why `PYTHONUNBUFFERED=1` is useful
- [x] explained why image hygiene matters

--- 
### Day 11 checklist (Docker Compose and multi-service local environments)

Today’s key messages are:
- **In Docker Compose, each service is its own containerized environment, and services usually communicate through the Compose network by service name, not by localhost.**
- Real applications often need multiple services, not just one container.
- Docker Compose defines and runs multi-container applications from a single file.
- In Compose networking, services usually reach each other by service name.
- Inside the API container, the database hostname should be `db`, not `localhost`.
- Named volumes help persist database data across container recreation.

The checklist:

- [x] updated `settings.py` with `database_url`
- [x] updated `main.py` to show `database_url`
- [x] updated `.env.example`
- [x] created `docker-compose.yml`
- [x] ran `docker compose up --build`
- [x] tested `/`
- [x] tested `/health`
- [x] inspected services with `docker compose ps`
- [x] stopped stack with `docker compose down`
- [x] understood why `db` is used instead of `localhost`

--- 
### Day 12 checklist (Compose workflows, service lifecycle, volumes, and stack debugging)

Today’s key messages are:
- **A multi-service stack should be debugged service by service, with attention to lifecycle state, logs, networking, and persistent volumes.**
- Operating a multi-service stack requires checking services individually, not as one undifferentiated system.
- `docker compose ps` and `docker compose logs` are core debugging tools for Compose stacks.
- `docker compose stop`, `docker compose down`, and `docker compose down -v` have very different effects.
- Named volumes allow database data to persist across container recreation.
- Service-specific logs help distinguish API problems from database problems.

The checklist:

- [x] started stack with `docker compose up -d --build`
- [x] inspected services with `docker compose ps`
- [x] inspected all logs with `docker compose logs`
- [x] inspected API logs with `docker compose logs api`
- [x] inspected DB logs with `docker compose logs db`
- [x] followed API logs while sending requests
- [x] inspected volumes with `docker volume ls`
- [x] tested `docker compose stop` and `docker compose start`
- [x] tested `docker compose down` and `docker compose up -d`
- [x] understood the effect of `docker compose down -v`

---
### Day 13 checklist (Compose networking, service names, and why localhost breaks between containers)

Today’s key messages are:
- **In a Compose stack, containers talk to each other through the internal Compose network by service name, while localhost only refers to the current container itself.**
- In Docker Compose, each service runs in its own containerized environment.
- Inside a container, `localhost` means that same container, not another service.
- Services in the same Compose network usually reach each other by service name.
- The API should use `db:5432` to reach PostgreSQL, not `localhost:5432`.
- Host access and container-to-container access are different network paths.

The checklist:

- [x] confirmed `DATABASE_URL` uses `db:5432`
- [x] started stack with `docker compose up -d --build`
- [x] tested `/` and verified DB URL in the API response
- [x] inspected services with `docker compose ps`
- [x] inspected Compose networks with `docker network ls`
- [x] inspected the project network with `docker network inspect`
- [x] entered the API container and checked environment variables
- [x] explained why `localhost` is wrong between containers
- [x] explained why service names work inside Compose

---
### Day 14 checklist (Compose environment files, overrides, and configuration strategy)

Today’s key messages are:
- **In a Compose stack, configuration should be understood by layer: app-level env loading, Compose service runtime env injection, and Compose YAML substitution are related but distinct mechanisms.**
- Configuration in a Compose setup exists at multiple layers and should be kept conceptually separate.
- The app’s local `.env` and a Compose service `env_file` are related, but they are not the same thing.
- `env_file` injects environment variables into a service container at runtime.
- `${VAR}` syntax in `docker-compose.yml` is Compose-side variable substitution, which is different from service runtime env injection.
- Variables used in `${VAR}` must be available to Compose itself, not only inside a service `env_file`.
- Cleaner configuration structure makes multi-service setups easier to reason about.

The checklist:

- [x] created `.env.compose.api`
- [x] created `.env.compose.db`
- [x] updated `docker-compose.yml` to use `env_file`
- [x] created `.env.compose.api.example`
- [x] added `.env.compose.api` to `.gitignore`
- [x] added `.env.compose.api` to `.dockerignore`
- [x] restarted stack with `docker compose up -d --build`
- [x] tested `/`
- [x] inspected API container environment variables
- [x] explained app `.env` vs Compose `env_file`
- [x] explained `env_file` vs `${VAR}` YAML substitution
- [x] understood why `API_PORT` and `DB_PORT` should not come only from service `env_file` files

--- 
### Day 15 checklist (First real database integration with PostgreSQL in Compose)

Today’s key messages are:
- **A dependency is not truly healthy just because its container is running — the application must be able to connect to it and perform a real operation.**
- A running DB container and a configured DB URL do not prove the API can actually query the database.
- A real dependency check requires the application to establish a connection and execute a query.
- `/health` and `/health/db` can represent different levels of system health.
- In Compose, the correct database hostname for the API is the DB service name, such as `db`.
- `depends_on` helps startup ordering, but does not guarantee database readiness.

The checklist:

- [x] installed `sqlalchemy` and `psycopg[binary]`
- [x] updated `requirements.txt`
- [x] created `db.py`
- [x] updated `main.py` with `/health/db`
- [x] rebuilt stack with `docker compose up -d --build`
- [x] tested `/health`
- [x] tested `/health/db`
- [x] inspected API logs
- [x] inspected DB logs
- [x] verified `DATABASE_URL` inside the API container
- [x] observed failure when DB hostname was intentionally broken

---

### Day 16 checklist (Persisting real data with PostgreSQL from the API)

Today’s key messages are:
- **A database-backed application is fundamentally different from an in-memory application because its state can survive process restarts and be retrieved later.**
- In-memory application state disappears when the process restarts, but persisted database state can survive restarts.
- A real database-backed API should insert, read, and update rows in PostgreSQL rather than only modifying Python memory.
- Application startup can be used to perform simple schema initialization in a learning project.
- `/health/db` proves connectivity, while task endpoints prove meaningful persistence behavior.
- Docker volumes are what allow PostgreSQL data to survive container recreation.

The checklist:

- [x] replaced in-memory task storage with PostgreSQL-backed queries
- [x] updated `db.py` with table initialization and task queries
- [x] updated `main.py` to use DB-backed task operations
- [x] rebuilt stack with `docker compose up -d --build`
- [x] tested `/health/db`
- [x] created a task in PostgreSQL
- [x] listed tasks from PostgreSQL
- [x] marked a task as done in PostgreSQL
- [x] restarted the stack without removing volumes
- [x] verified task data still existed after restart
- [x] optionally inspected the `tasks` table directly in PostgreSQL

---

### Day 17 checklist (Database schema lifecycle, startup risks, and why migrations exist)

Today’s key messages are:
- **Bootstrapping a database and evolving a database schema are not the same task — schema evolution requires explicit, controlled changes, which is why migrations exist.**
- A database schema defines the structure of tables, columns, and constraints, while data is the content stored inside that structure.
- `CREATE TABLE IF NOT EXISTS` is useful for first-time bootstrap, but it does not evolve an already existing table.
- Changing schema definition code is not the same as migrating an existing database.
- Real projects use migrations to apply schema changes in a controlled, versioned way.
- Application startup logic and database schema lifecycle management are related but distinct responsibilities.

The checklist:

- [x] inspected the `tasks` table schema with `psql`
- [x] inspected stored task data with `SELECT * FROM tasks`
- [x] explained schema vs data
- [x] explained why startup table creation is useful for bootstrap
- [x] explained why startup table creation is not enough for schema evolution
- [x] understood why migrations exist
- [x] understood why changing `CREATE TABLE IF NOT EXISTS` does not update an existing table

---
### Day 18 checklist (Docker Compose for development vs runtime)

Today’s key messages are:
- **A good container workflow often uses a clean base stack for runtime-like behavior and a separate override for development convenience such as bind mounts and live reload.**
- A Compose stack can be optimized either for development speed or for cleaner runtime-like behavior.
- A runtime-oriented stack usually avoids live reload and source bind mounts.
- A development-oriented stack often uses bind mounts and `--reload` for faster iteration.
- Compose override files are a clean way to add dev-only behavior without polluting the base stack.
- Bind mounts improve speed for coding, but make the container depend more directly on host file state.

The checklist:

- [x] kept `docker-compose.yml` as the base runtime-style file
- [x] created `docker-compose.dev.yml`
- [x] started the stack with both Compose files
- [x] enabled `--reload` for the API in dev mode
- [x] mounted local source code into the API container
- [x] edited code and observed live reload without rebuilding
- [x] compared dev-style and runtime-style Compose behavior
- [x] explained why bind mounts are useful in development
- [x] explained why bind mounts reduce runtime reproducibility