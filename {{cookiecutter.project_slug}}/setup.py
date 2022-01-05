"""The setup script."""

from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="{{ cookiecutter.project_slug }}",
    install_requires=[
        {% if cookiecutter.command_line_interface|lower == 'click' -%}'Click>=7.0',{%- endif %}
        {% if cookiecutter.git_init == "y" and cookiecutter.add_pre_commit_hooks == "y" -%}'pre-commit',{%- endif %}
    ],
)
