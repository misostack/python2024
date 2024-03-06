# Python tutorial 2024

## Glossary

### Python Entry Level

- Python Basic Part 0 - Syntax
- Python Basic Part 1 - Strings
- Python Basic Part 2 - List, Tuple, Dictionary
- Python Basic Part 3 - Functions, Generators, Scope
- Python Basic Part 4 - Lambda
- Python Basic Part 5 - Modules, OOP
- Python Basic Part 6 - Exception
- Python Basic Part 7 - File I/O
- Python Basic Part 8 - Build Notification API with Flask + Firebase + Chrome Extension

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

## Tips & Tricks

### DateTime

- https://www.programiz.com/python-programming/datetime/timestamp-datetime
- https://www.datacamp.com/tutorial/converting-strings-datetime-objects
- https://www.geeksforgeeks.org/how-to-convert-timestamp-string-to-datetime-object-in-python/
