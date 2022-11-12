# kisaragi-auth-component
REST API for authorization on Kisaragi project

## Run the project
```sh
uvicorn --port 5000 --host 127.0.0.1 main:app --reload --log-config log.ini
```
## Run tests
Run Tests
```sh
pytest
```
Run Coverage Test
```sh
pytest --cov
```