# Pybase RSS Tools

> A tool to fetch rss feed and parse data into json, save as json file.

## Fun fact

- Python is a intepreter language, but it was compiled into intermediary form(bytecode) and then execute

- [What is byte code](https://www.techtarget.com/whatis/definition/bytecode)

## Development

### Install Poetry

- https://python-poetry.org/docs/#installing-with-the-official-installer

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
```

### Adjust poetry venv path

```sh
poetry config virtualenvs.in-project true
poetry new python2024
cd python2024
poetry install
```

### Some poetry command

```sh
poetry env info
poetry env info --path
```
