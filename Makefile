install:
	pip install -r requirements.txt


jwt_secret_key: 
	python -c "import secrets;print(f'JWT_SECRET_KEY=\"{secrets.token_urlsafe(64)}\"')" >> .secrets.toml


set_env:
	cp .env.sample .env 
	cp .secrets.toml.sample .secrets.toml
	make jwt_secret_key
	make install
	

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info


lint:
	pip install -r requirements-dev.txt
	black .
	flake8 .


test:
	pytest -vv 


coverage:
	pytest --cov=api


run:
	flask run


crontab: install
	flask crontab add
	crontab -l


crontab-remove:
	flask crontab remove


set_prod:
	sudo apt update
	sudo apt install git

	sudo apt install -y python3-pip
	sudo apt install build-essential libssl-dev libffi-dev python3-dev
	sudo apt install -y python3-venv

	python3.7 -m venv env