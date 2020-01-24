# flaskblueprint

An Authentication Server and TargetGroupResposeSchema Manager.

![Build Status](https://github.com/gabicavalcante/flaskblueprint/workflows/CI/badge.svg)
[![Code Coverage](https://codecov.io/gh/gabicavalcante/flaskblueprint/branch/master/graphs/badge.svg?token=BlrDDl2SJq)](https://codecov.io/gh/gabicavalcante/flaskblueprint)

### makefile

We made a `makefile` to help you with you setup project. Check the file to see all commands availables.

### create and active virtualenv

```
# virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
# pyenv
$ pyenv virtualenv 3.7.4 flaskblueprint
$ pyenv activate flaskblueprint
```

### install requirements

```
$ cd flaskblueprint
$ pip install -r requirements-dev.txt
```

_note_: `requirements-dev.txt` has all requirements packages to test, coverage and lint. If you don't want this packages, just run `pip install -r requirements.txt`.

### create and configure .env file

```
$ touch .env
```

add the env vars:

```
FLASK_APP=flaskblueprint.app
FLASK_ENV='development'
FLASK_DEBUG=1
SECRET_KEY="s3cr3t"
DATABASE_URL="postgresql://localhost/flaskblueprint_db"
```

### migrate

```
$ flask db init
$ psql -U postgres
psql (11.4)
Type "help" for help.

postgres=# create database flaskblueprint_db
$ flask db migrate
$ flask db upgrade
```

### run

```
$  flask run
```

```
# secrets.toml
[default]
CSRF_SESSION_KEY = ""
JWT_SECRET_KEY = ""
TOKEN_SGP = ""
APP = ""
```

### references

- flask migrate https://flask-migrate.readthedocs.io/en/latest/
- precommit https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
