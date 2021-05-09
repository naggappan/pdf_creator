# pdf_creator
A tool to create a pdf document based on inputs

# dev setup
Here we are using a python virtual env via pipenv and not the virtual env and hence using Pipfile and Pipfile.lock to manage dependency and not requirements.txt. Please follow the below step to install these dependency in linux machine

#### `pyenv`

Install `pyenv`, a tool to manage multiple Python versions. It is a fork of `rbenv` and `ruby-build`,
which do the same for Ruby. It installs these Python versions into your home directory, so
doesn't require `sudo` or any other system-level manipulation.

For Linux systems [`pyenv-installer`](https://github.com/pyenv/pyenv-installer/) has been generally recommended, but we
suggest reviewing the current [install instructions](https://github.com/pyenv/pyenv#installation) in case the guidance has changed.

See [common build problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems) if you have trouble installing.

Once that's complete, don't forget to update your shell config file (e.g. `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc`)
as described in the installation instructions.

#### Python 3

Install the latest Python 3.x.y release with `pyenv` that matches our current version requirements and activate it as
your global default. You can also use `pyenv` to set your current shell's Python version (`pyenv shell`), or for a
specific folder (`pyenv local`).

For example, if the current convention is to use Python 3.8 and the latest release is 3.8.8:

```
$ pyenv install 3.8.8
$ pyenv global 3.8.8
```

Make sure your current `pip` and `setuptools` for Python 3.x.y are up-to-date.

```
$ python -m pip install --upgrade pip setuptools
```

Note that once you start using a `pyenv`-managed Python install for other tools below (e.g. those installed with `pipx`),
uninstalling that Python version from `pyenv` will break those tools! Refer to the `pipx` notes for how to manage `pipx`
when upgrading Python versions.

#### `pipx`

Install [pipx](https://pipxproject.github.io/pipx/), a tool for installing Python command-line scripts (not libraries)
in their own isolated environments.

```
$ python3 -m pip install --user pipx
```

Prepend `~/.local/bin` to your `PATH` env var if it isn't there already:

```
$ python3 -m userpath prepend ~/.local/bin
```

Or manually add the following to your shell config file (e.g. `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc`) and reload your shell:

```shell
export PATH=~/.local/bin:$PATH
```

note: we prepend to `PATH` so that it is searched before any pre-existing system-level Python paths

##### `pipx` and Python Upgrades

`pipx` is one of the only packages you'll install globally, since `pipx` lets you package isolate almost everything else.
Unforunately this means that when you upgrade the Python that `pipx` was installed to it breaks both `pipx` and
evverything installed with `pipx`.

You can account for this by following this process when upgrading, shown below with an example upgrade from `3.8.7` to `3.8.8`:

```shell
$ python -m pip uninstall pipx

$ pyenv install 3.8.8
$ pyenv global 3.8.8
$ pyenv uninstall 3.8.7

$ python -m pip install --user pipx

# restart or source your shell to ensure reinstalled `pipx` is usable

# reinstalls all tools currently installed in `pipx` to use the new Python version
$ pipx reinstall-all
```

note: removing `pipx` isn't _strictly_ necessary if you're only upgrading a patch release, but if you're upgrading to
a new minor release (e.g. `3.8.x` -> `3.9.x`) then you will need to reinstall, so it's easier to just doc doing it.

#### `pipenv`

Install `pipenv`, a tool to manage Python package dependencies for applications.

```
$ pipx install pipenv
```

Add the following to your shell config file e.g. `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc` and reload your shell.

```shell
export PIPENV_PYTHON="$PYENV_ROOT/shims/python"
```


# How to start the app locally?

```shell
git clone <this repo>
cd npdf_creator
pipenv install
pipenv shell
cd mysite
python manage.py runserver 0.0.0.0:8080
```

When you start the server locally open the browser and make sure you are able to access the service using url http://localhost:8080/docwrite

Now as a next step do the migrations and setup the admin superuser credentials with below steps

```shell script
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

To confirm your migration is done and able to access the admin page start the runserver command again and hit the url http://localhost:8080/admin and use your super user to login


