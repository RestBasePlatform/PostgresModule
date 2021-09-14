import socket
from restbase_types import DatabaseConnectionData


async def health_check(db_con_data: DatabaseConnectionData) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((db_con_data.host, db_con_data.port))

    if result != 0:
        return False
    return True
