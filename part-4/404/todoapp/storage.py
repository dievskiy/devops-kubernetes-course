from __future__ import annotations

import psycopg2
import os
from psycopg2 import Error as DBError
from typing import List, Optional

HOST = os.getenv('HOST', 'localhost')


def _get_db_connection():
    conn = psycopg2.connect(host=HOST,
                            database=os.environ['POSTGRES_DB'],
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'])
    return conn


def check_connection() -> bool:
    try:
        _get_db_connection()
        return True
    except psycopg2.Error:
        return False


def fetch_todos() -> List[Optional[str]] | None:
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute('select * from todos;')
        todos = cur.fetchall()
        cur.close()
        con.close()
        if not todos:
            return []
        todos = [todo[1] for todo in todos]
        return todos
    except DBError as err:
        print(f'Error while selecting data {err}')
        return None


def init_db():
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute(
            f'create table todos (id SERIAL PRIMARY KEY not null, name varchar(140) not null)')
        con.commit()
        con.close()
    except Exception:
        print('Table already exists')


def save_todo(new_todo: str) -> bool:
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute(f"insert into todos (name) values ('{new_todo}');")
        con.commit()
        cur.close()
        con.close()
        print(f'Saved new todo to the database [{new_todo}]')
        return True
    except DBError as err:
        print(f'Error while inserting data{err}')
        return False
