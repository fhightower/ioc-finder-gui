# IOC Finder GUI

**NOTE: This project is archived as we now have [interactive documentation](https://hightower.space/ioc-finder/) which you can use to test the `ioc-finder` package.**

---

[![Build Status](https://travis-ci.org/fhightower/ioc-finder-gui.svg?branch=master)](https://travis-ci.org/fhightower/ioc-finder-gui)

GUI for the indicator of compromise project: [http://ioc-finder.hightower.space](http://ioc-finder.hightower.space).

## Credits

This app was created with the flask template here: [https://gitlab.com/fhightower-templates/flask-template](https://gitlab.com/fhightower-templates/flask-template). Thanks to [cookiecutter](https://github.com/audreyr/cookiecutter), a project for creating project templates.

## Running the App Locally

After cloning the repo...

To create a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for the app, run:

```
make venv
```

Clone the app and run the application at [http://127.0.0.1:5000/](http://127.0.0.1:5000/):

```
make run
```

To test the app, run:

```
make test
```
