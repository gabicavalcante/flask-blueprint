# flaskblueprint

![Build Status](https://github.com/gabicavalcante/flask-blueprint/workflows/CI/badge.svg)
[![Code Coverage](https://codecov.io/gh/gabicavalcante/flask-blueprint/branch/master/graphs/badge.svg?token=BlrDDl2SJq)](https://codecov.io/gh/gabicavalcante/flaskblueprint)

This is a simple flask blueprint, to help you to start a new project with a few importants features.

### makefile

We made a `makefile` to help you with you setup project. Check the file to see all commands availables.

### python code formartter

- [`black`](https://github.com/psf/black)
- [`flake8`](http://flake8.pycqa.org/en/latest/)
- [`pre-commit`](https://pre-commit.com/): the file `.pre-commit-config.yml` is a file to configure git hooks for identify simple issues before submit a commit. Run `pre-commit install` to set up the git hook scripts. After that, `pre-commit` will run automatically on `git commit`.

### libs

- config: [`dynaconf`](https://dynaconf.readthedocs.io/en/latest/)
 - _dynaconf a layered configuration system for Python applications_. It's a great libary to manager the configuration files of your Python Project.
- admin: [`flask_admin`](https://flask-admin.readthedocs.io/en/latest/)
 - Build an admin interface on top of yours data models. 
- auth: [`flask_simplelogin`](https://github.com/flask-extensions/flask_simplelogin)
- commands: [`click`](https://flask.palletsprojects.com/en/1.0.x/cli/)
 - You can create commands with click to simplify tasks.
- tests: [`pytest`](https://docs.pytest.org/en/latest/)
- token: [`flask_jwt_extended`](https://flask-jwt-extended.readthedocs.io/en/stable/)
- log: [`logging`](https://flask.palletsprojects.com/en/1.0.x/logging/)
- db: [`flask_sqlalchemy`](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) and [`flask_migrate`](https://flask-migrate.readthedocs.io/en/latest/)
- appearance: [`flask_bootstrap`](https://pythonhosted.org/Flask-Bootstrap/)

### coverage report

- [codecov](https://codecov.io/gh/gabicavalcante/flaskblueprint)

### continuous code quality

- [sonar](https://sonarcloud.io/dashboard?id=gabicavalcante_flaskblueprint)

## setup

### create and configure .env file

```
$ cp .env.sample .env
```

add the env vars:

```
FLASK_APP=flaskblueprint.app:create_app
SECRET_KEY="..."
FLASK_ENV=development
```

### create and configure .secrets.toml

```
$ cp .secrets.toml.sample .secrets.toml
```

```
[default]
CSRF_SESSION_KEY = ""
JWT_SECRET_KEY = ""
```

### configure the .settings.toml

Open the .settings.toml file and check all variables. See if you want change any thing. I set the `SQLALCHEMY_DATABASE_URI` to connect with the mysql credentials that I defined in docker-compose file. If you change one of these files, remenber to change other.

## run

### docker-compose

You can run the app using the docker-compose file.

```
$  docker-compose up --build
```

### flask run

#### virtualenv

```
# virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
# pyenv
$ pyenv virtualenv 3.7.4 flaskblueprint
$ pyenv activate flaskblueprint
```

#### install requirements

```
$ cd flaskblueprint
$ pip install -r requirements-dev.txt
```

_note_: `requirements-dev.txt` has all requirements packages to test, coverage and lint. If you don't want this packages, just run `pip install -r requirements.txt`.

#### migrate

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

#### run

```
$  flask run
```

## tests

Start the test db:

```
$  docker-compose up database-test
```

To run tests with coverage

```
$  pytest --cov=flaskblueprint
```

### references

- flask migrate https://flask-migrate.readthedocs.io/en/latest/
- precommit https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
