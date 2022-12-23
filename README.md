# kisaragi-auth-component
REST API for authorization on Kisaragi project

## Software Requirements
- Python 3.x
- pip package manager
- virtualenv package

## Run the project
### 1. Create Python Virtual Environment
```sh
python3 -m venv venv
```
### 2. Activate the VENV
Powershell:
```sh
python3 -m venv ./
./venv/Scripts/Activate.ps1
```
CMD:
```sh
.\venv\Scripts\activate.bat
Bash:
$ source <venv>/bin/activate
```
### 3. Install Requirements
```sh
pip install -r requirement.txt
```
### 4. Obtain the .env file
For more info read [.env.example](./.env.example)
### 5. Execute UVICORN
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