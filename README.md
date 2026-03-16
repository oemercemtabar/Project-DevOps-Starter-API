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
