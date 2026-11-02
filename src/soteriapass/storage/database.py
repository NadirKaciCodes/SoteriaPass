import sqlite3
from pathlib import Path
from platformdirs import user_data_dir


APP_NAME = "SoteriaPass"

def get_database_path():
    data_directory = Path(user_data_dir(APP_NAME))
    data_directory.mkdir(parents=True, exist_ok=True)

    return data_directory / "soteriapass.db"

def get_connection():

    database_path = get_database_path()
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    return connection

def initialise_database():

    with get_connection() as connection :
        connection.execute("""
            CREATE TABLE IF NOT EXISTS vault_metadata (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                salt BLOB NOT NULL,
                kdf_paramaters TEXT NOT NULL,
                wrapped_vault_key BLOB NOT NULL,
                key_nonce BLOB NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS vault_entries(
                id TEXT PRIMARY KEY,
                encrypted_data BLOB NOT NULL,
                nonce BLOB NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)