import sqlalchemy
import configparser
from sqlalchemy.orm import sessionmaker
import pytest
from urllib.parse import quote

@pytest.fixture(scope='session')
def db_engine():
    config = configparser.ConfigParser()
    config.read('pytest.ini')
    connectionStr = "mariadb+mariadbconnector://{}:{}@{}:{}/{}"\
        .format(config['pytest']['mysql_user'], quote(config['pytest']['mysql_passwd']),
        config['pytest']['mysql_host'], config['pytest']['mysql_port'], config['pytest']['mysqldbname'])
    engine = sqlalchemy.create_engine(connectionStr)
    yield engine
    engine.dispose()

@pytest.fixture(scope='function')
def rollback_session(db_engine):
    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()