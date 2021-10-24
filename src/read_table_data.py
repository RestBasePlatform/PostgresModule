from collections import namedtuple
from typing import List

from sqlalchemy import create_engine

from restbase_types import DatabaseConnectionData
from restbase_types import DatabaseTable


GET_TABLE_DATA_REQUEST = """
        SELECT column_name, data_type, table_schema, table_name FROM information_schema.columns
    """
# where table_schema <> 'pg_catalog' and table_schema <> 'information_schema'

GET_TABLE_DATA_REQUEST_NT = namedtuple(
    "GET_TABLE_DATA_REQUEST_NT",
    ("column_name", "table_name", "data_type", "schema", "database"),
)

LIST_DATABASE_REQUEST = """
    SELECT datname FROM pg_database
    WHERE datistemplate = false;
"""


_con_data = DatabaseConnectionData(
    host="10.0.0.6", port="5432", username="postgres", password="mysecretpassword"
)


def read_table_data(con_data: DatabaseConnectionData) -> List[DatabaseTable]:
    engine = create_engine(con_data.get_sqlalchemy_string_without_database_())
    db_list = list([i[0] for i in engine.execute(LIST_DATABASE_REQUEST)])
    for db in db_list:
        sql_alchemy_row_with_db = (
            con_data.get_sqlalchemy_string_without_database_() + f"/{db}"
        )
        db_engine = create_engine(sql_alchemy_row_with_db)
        columns_list = list(
            [
                GET_TABLE_DATA_REQUEST_NT(i[0], i[3], i[1], i[2], db)
                for i in db_engine.execute(GET_TABLE_DATA_REQUEST)
            ]
        )
        print(columns_list)


read_table_data(_con_data)
