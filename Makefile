clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log* && rm -fr .cache && rm -rf .pytest_cache

venv:
	virtualenv -p python3 ~/.virtualenvs/ioc_finder_gui && . ~/.virtualenvs/ioc_finder_gui/bin/activate && pip3 install -r requirements.txt

run:
	~/.virtualenvs/ioc_finder_gui/bin/python ioc_finder_gui/ioc_finder_gui.py

test: clean
	~/.virtualenvs/ioc_finder_gui/bin/python -m pytest

destroy:
	rm -rf ~/.virtualenvs/ioc_finder_gui

init:
	. ~/.virtualenvs/ioc_finder_gui/bin/activate && ~/.virtualenvs/ioc_finder_gui/bin/python ioc_finder_gui/manage.py db init

mg:
	~/.virtualenvs/ioc_finder_gui/bin/python ioc_finder_gui/manage.py db migrate

up:
	~/.virtualenvs/ioc_finder_gui/bin/python ioc_finder_gui/manage.py db upgrade
