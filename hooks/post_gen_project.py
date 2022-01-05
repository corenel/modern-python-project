#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.abspath(os.path.realpath(os.path.curdir))


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")
        remove_file("docs/authors.md")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{ cookiecutter.git_init }}" == "y":
        os.system(f"cd {PROJECT_DIRECTORY} && git init")
        os.system(
            "cd {} && git remote add origin {}".format(
                PROJECT_DIRECTORY, "{{ cookiecutter.git_remote_repository }}"
            )
        )
        os.system(f"cd {PROJECT_DIRECTORY} && git add .")
        os.system(f'cd {PROJECT_DIRECTORY} && git commit -m "chore: initial commit"')

        if "{{ cookiecutter.add_pre_commit_hooks }}" == "y":
            os.system(
                f"cd {PROJECT_DIRECTORY} && pip install -U pre-commit && pre-commit install"
            )

        if "{{ cookiecutter.add_commit_msg_hook }}" == "y":
            os.system(f"cd {PROJECT_DIRECTORY} && ./tools/install_git_hooks.sh")
