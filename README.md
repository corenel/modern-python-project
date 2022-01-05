# modern-python-project

Yet another [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python package.

## Features

- Testing setup with [unittest](https://docs.python.org/3/library/unittest.html) or [pytest](https://docs.pytest.org/).
- [Tox](https://tox.wiki/en/latest/) testing: Setup to easily test for Python 3.6 and newer
- Git hooks for [pre-commit](https://pre-commit.com/) and commit-msg.
- [Sphinx](https://www.sphinx-doc.org/) docs: Documentation ready for generation with, for example, [Read the Docs](https://readthedocs.io/).
- (optional) Command line interface using [Click](https://github.com/pallets/click).

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/corenel/modern-python-project.git
```

And then:

1. Create a blank remote repo and push to it.
2. Install the dev requirements into a `virtualenv` or `conda` environment. (`pip install -r requirements_dev.txt`)
3. Add a `requirements.txt` file that specifies the packages you will need for your project and their versions. For more info see the [pip docs for requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
4. Start coding!

## Advanced Usage

### Build Documentation

```bash
cd /path/to/your/project
make docs
```

## Acknowledgements

- [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
