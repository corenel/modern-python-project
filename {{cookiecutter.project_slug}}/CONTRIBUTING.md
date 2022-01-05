# How to contribute to bdca-visionsense-server

Thank you for considering contributing to `{{ cookiecutter.project_slug }}`!

## Submitting patches

Include the following in your patch:

- Use [Black](https://black.readthedocs.io/) to format your code. This and other tools will run automatically if you install [pre-commit](https://pre-commit.com/) using the instructions below.
- Include tests if your patch adds or changes code. Make sure the test fails without your patch.
- Update any relevant docs pages and docstrings. Docs pages and docstrings should be wrapped at 72 characters.

### First time setup

- Download and install the [latest version of git](https://git-scm.com/downloads).

- Configure git with your [username](https://docs.github.com/en/github/using-git/setting-your-username-in-git) and [email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address).

  ```bash
  git config --global user.name 'your name'
  git config --global user.email 'your email'
  ```

- Make sure you have a [GitHub account](https://github.com/join).

- [Clone](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork) the main repository locally.

  ```bash
  git clone {{ cookiecutter.git_remote_repository }}
  cd {{ cookiecutter.project_slug }}
  ```

- Create a [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) virtual environment.

  ```bash
  conda create -n {{ cookiecutter.project_slug }} python=3.7
  conda activate {{ cookiecutter.project_slug }}
  ```

- Upgrade `pip` and `setuptools`.

  ```bash
  python -m pip install --upgrade pip setuptools
  ```

- Install the development dependencies, then install `{{ cookiecutter.project_slug }}` in editable mode.

  ```bash
  pip install -r requirements_dev.txt && pip install -e .
  ```

- Install the `pre-commit` hooks.

  ```bash
  pre-commit install
  ```

- Install the `commit-msg` hook.

  ```bash
  ./tools/install_git_hooks.sh
  ```

### Start coding

- Create a branch to identify the issue you would like to work on.

  ```bash
  git fetch origin
  git checkout -b your-branch-name origin/master
  ```

- Using your favorite editor, make your changes.

- Write your commit message with one of the following prefixes, e.g. `feat: add support for PyTorch`. This is based on the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/#summary)

  - `feat`: (new feature for the user, not a new feature for build script)
  - `fix`: (bug fix for the user, not a fix to a build script)
  - `docs`: (changes to the documentation)
  - `style`: (formatting, missing semicolons, etc; no production code change)
  - `refactor`: (refactoring production code, eg. renaming a variable)
  - `perf`: (code changes that improve performance)
  - `test`: (adding missing tests, refactoring tests; no production code change)
  - `chore`: (updating grunt tasks etc; no production code change)
  - `build`: (changes that affect the build system or external dependencies)
  - `ci`: (changes to configuration files and scripts)
  - `revert`: (reverts a previous commit)

- Include tests that cover any code changes you make. Make sure the test fails without your patch. Run the tests as described below.

- Push your commits to your branch on GitHub and [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
