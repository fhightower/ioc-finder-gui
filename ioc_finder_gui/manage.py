#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from ioc_finder_gui import app, db


app.config.from_pyfile('config.py')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
