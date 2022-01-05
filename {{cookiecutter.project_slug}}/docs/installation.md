# Installation

## Stable release

To install {{ cookiecutter.project_name }}, run this command in your
terminal:

```bash
pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install {{ cookiecutter.project_name }},
as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/)
can guide you through the process.

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from
the [Github repo][{{ cookiecutter.git_remote_repository }}].

You can either clone the public repository:

```bash
git clone {{ cookiecutter.git_remote_repository }}
```

Once you have a copy of the source, you can install it with:

```bash
python setup.py install
```
