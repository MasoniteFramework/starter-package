# Starter Package

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="130px">
</p>

<p align="center">
  <a href="https://docs.masoniteproject.com">
    <img alt="Masonite Package" src="https://img.shields.io/static/v1?label=Masonite&message=package&labelColor=grey&color=blue&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAAA6gAwAEAAAAAQAAAA4AAAAATspU+QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAnxJREFUKBVNUl1IVEEUPjPObdd1VdxWM0rMIl3bzbVWLSofVm3th0AhMakHHyqRiNSHEAq5b2HSVvoQRUiEECQUQkkPbRslRGigG8auoon2oPSjpev+3PWeZq7eaC5nDt93vplz5txDQJYpNxX4st4JFiwj9aCqmswUFQNS/A2YskrZJPYefkECC2GhQwAqvLYybwXrwBvq8HSNOXRO92+aH7nW8vc/wS2Z9TqneYt2KHjlf9Iv+43wFJMExzO0YE5OKe60N+AOW6OmE+WJTBrg23jjzWxMBauOlfyycsV24F+cH+zAXYUOGl+DaiDxfl245/W9OnVrSY+O2eqPkyz4sVvHoKp9gOihf5KoAVv3hkQgbj/ihG9fI3RixKcUVx7lJVaEc0vnyf2FFll+ny80ZHZiGhIKowWJBCEAKr+FSuNDLt+lxybSF51lo74arqs113dOZqwsptxNs5bwi7Q3q8npSC2AWmvjTncZf1l61e5DEizNn5mtufpsqk5+CZTuq00sP1wkNPv8jeEikVVlJso+GEwRtNs3QeBt2YP2V2ZI3Tx0e+7T89zK5tNASOLEytJAryGtkLc2PcBM5byyUWYkMQpMioYcDcchC6xN220Iv36Ot8pV0454RHLEwmmD7UWfIdX0zq3GjMPG5NKBtv5qiPEPekK2U51j1451BZoc3i+1ohSQ/UzzG5uYFFn2mwVUnO4O3JblXA91T51l3pB3QweDl7sNXMyEjbguSjrPcQNmwDkNc8CbCvDd0+xCC7RFi9wFulD3mJeXqxQevB4prrqgc0TmQ85NG/K43e2UwnMVAJIEBNfWRYR3HfnvivrIzMyo4Hgy+hfscvLo53jItAAAAABJRU5ErkJggg==">
  </a>
  <img alt="GitHub Workflow Status (branch)" src="https://img.shields.io/github/workflow/status/MasoniteFramework/starter-package/Test%20Application/master">
  <img alt="Coveralls github branch" src="https://img.shields.io/coveralls/github/MasoniteFramework/starter-package/master">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/starter-package">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/MasoniteFramework/starter-package">
  <img alt="License" src="https://img.shields.io/github/license/MasoniteFramework/starter-package">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

---

**This is a template repository for crafting quality Masonite packages: [🔨 Craft Package](https://github.com/MasoniteFramework/starter-package/generate)**

## Crafting and Developing

### Choosing a package name

To have a consistent Masonite package ecosystem, it is advised to follow those guidelines:

- The verbose/human name of your package should start with `Masonite` such as `Masonite API`, `Masonite Events`, `Masonite Nice Package`.
- You can slugify this name to get a Python package name (installable with pip). All Masonite packages should have a
  Python package name starting with **masonite-** such as `masonite-api`, `masonite-events`, `masonite-nice-package`.
- A package should be imported from `masonite` namespace:

```python
from masonite.api import X  # masonite-api
from masonite.events import Y  # masonite-events
from masonite.nice_package import Z  # masonite-nice-package
```

### Selecting a crafting option

**A. Craft a Masonite package with this Github template**

Click on 🔨 Craft Package at top to create a repository from this template, then clone it.

To setup your package and get your package up and running:

1. you should first take a look at `setup.py` and make any packages specific changes there. These include the classifiers and package name.
2. you should also update package name and description in :

- setup.py
- makefile
- CONTRIBUTING.md
- README.md
  - update package name and slug
  - remove _Crafting and Developing_ section
- src/masonite:
  - rename the directory `package` to your Python package name
  - rename `PackageProvider` if your package needs a ServiceProvider
  - update `PackageProvider` import in `src/masonite/{package}/__init__.py`
  - edit `config/package.py` filename and content if your package needs a config file

**B. Craft a Masonite package with cookiecutter**

You can also use Cookiecutter Masonite Package to automatically craft your package with correct naming and configuration: [🔨 Craft Package](https://github.com/girardinsamuel/cookiecutter-masonite-package).

### Dev Quick Start

Whatever crafting option you choose when your repository is created, you should start by creating a virtual environment and activate it:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Init dependencies (this will install Masonite, a few development related packages and the package itself):

```
$ make init
```

Finally you can run the tests and start building your application:

```
$ python -m pytest
```

You can start the test project in the repo to test your package at `http://localhost:8000/`:

```
$ python craft serve
```

**Setup coverage**

The repository is already setup to use `Coveralls` to publish the package coverage. You just need to:

1. Login/register on [coveralls.io](https://coveralls.io/).
2. Select your Github repository and enable coveralls.

Github CI will run tests, compute coverage and upload it to coveralls. The badge is already configured for
Coveralls and should display correctly at first coveralls score publish.

Of course you can use `codecov` if you prefer, you will have to edit Github workflow and the badge.

**Publish your package on PyPi**

To publish the package read the Official Documentation on [publishing package to PyPi](https://docs.masoniteproject.com/advanced/creating-packages#uploading-to-pypi).

A Github workflow is already configured to publish the package to PyPi when
a release is created. You just have to:

1. Login/register on [pypi.io](https://pypi.io/).
2. Add your credentials as Github Secrets in this repository: `PYPI_USERNAME` and `PYPI_PASSWORD`

More info in [Contributing Documentation](CONTRIBUTING.md).

---

## Introduction

_Add your package description here_

## Features

- _Add your package main features here_
- _and here_

## Official Masonite Documentation

New to Masonite ? Please first read the [Official Documentation](https://docs.masoniteproject.com/).
Masonite strives to have extremely comprehensive documentation 😃. It would be wise to go through the tutorials there.
If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](http://slack.masoniteproject.com/)!

## Installation

```bash
pip install package
```

## Configuration

Add PackageProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite.package import PackageProvider

# ...
PROVIDERS = [
    # ...

    # Third Party Providers
    PackageProvider,

    # ...
]
```

Then install OR publish the reqired package files (configuration, views ...):

```bash
python craft package:install
```

OR (depending on your preferences)

```bash
python craft publish PackageProvider
```

## Usage

_Explain how to use your package_

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## License

Your Package is open-sourced software licensed under the [MIT License](LICENSE).
