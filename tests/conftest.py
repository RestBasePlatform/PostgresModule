import os
import shutil
import sys

import pytest
from httpx import AsyncClient


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/")))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from restbase_types.connection import DatabaseConnectionData


def pytest_sessionstart():
    os.system("docker rm -f rb_test_postgres")
    os.system(
        "docker run --name rb_test_postgres -e POSTGRES_PASSWORD=password -d  -p 5432:5432 postgres"
    )


@pytest.fixture(scope="session")
def db_credentials() -> DatabaseConnectionData:
    return DatabaseConnectionData(
        host="localhost",
        port=5432,
        username="postgres",
        password="password",
        connection_kwargs={},
    )


# def pytest_sessionfinish(session, exitstatus):
#     os.system("docker rm -f rb_test_postgres")
