# mariadb
Mariadb modeling and testing

## Getting start

- In macos, install mariadb connector
- Reference [link](https://stackoverflow.com/a/44268445/7270469)

```
brew install mariadb-connector-c
ln -s /usr/local/opt/mariadb-connector-c/bin/mariadb_config /usr/local/bin/mysql_config

python3 -m venv db-env
```

## Test

Using pytest

Python == `3.9.1`

```
source db-env/bin/activate
pytest
```

- Export requirements list

```
pip3 freeze > requirements.txt
```

- Install requirements

```
pip3 install -r requirements.txt
```