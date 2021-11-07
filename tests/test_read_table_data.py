import asynctest
import pytest
from sqlalchemy import create_engine


@pytest.fixture(scope="session")
async def db_test_read_data_structure(db_credentials):
    engine = create_engine(db_credentials.get_sqlalchemy_string_without_database_())
    engine.execute("CREATE DATABASE test_read_data")


@pytest.mark.asyncio
async def test_read_data(db_credentials, db_test_read_data_structure):
    with asynctest.patch("read_table_data.read_table_data") as read_database_list_mock:
        read_database_list_mock.return_value = ["test_db_1", "test_db_2"]
