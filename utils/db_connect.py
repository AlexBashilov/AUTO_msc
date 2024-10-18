import os
import psycopg2
from typing import Text
from psycopg2._psycopg import connection

_connection = None


def open_connection() -> connection:
    global _connection
    if not _connection:
        try:
            _connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=get_db_port(os.getenv("STAGE")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
        except psycopg2.Error as e:
            raise Exception(f"Произошла ошибка '{e}' при подключении к базе данных")
    return _connection


def close_connection():
    global _connection
    if _connection:
        try:
            _connection.close()
        except psycopg2.Error as e:
            raise Exception(f"Произошла ошибка '{e}' при отключении от базы данных")
    return _connection


def get_db_port(stage) -> Text:
    stage = stage
    if len(stage) > 1:
        return f"100{stage}"
    return f"1000{stage}"
