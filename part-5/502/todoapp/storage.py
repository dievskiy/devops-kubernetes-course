from __future__ import annotations

import psycopg2
import os
from psycopg2 import Error as DBError
from typing import List, Optional, Any, Set, Dict

HOST = os.getenv('HOST', 'localhost')


def _get_db_connection():
    conn = psycopg2.connect(host=HOST,
                            database=os.environ['POSTGRES_DB'],
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'])
    return conn


def check_connection() -> bool:
    try:
        con = _get_db_connection()
        if con:
            con.close()
        return True
    except psycopg2.Error:
        return False


def toggle(todo_id: int, is_done: bool) -> bool:
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute(f'update todos set done={str(is_done)} where id={todo_id}')
        con.commit()
        return True
    except DBError as err:
        print(f'Error while setting a todo as done/undone {err}')
        return False


def fetch_todos() -> List[Dict[str, bool]] | None:
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute('select * from todos order by id desc;')
        todos = cur.fetchall()
        cur.close()
        con.close()
        if not todos:
            return []
        todos = [{"name": str(todo[1]), "is_done": bool(todo[2]), "id": int(todo[0])} for todo in todos]
        return todos
    except DBError as err:
        print(f'Error while selecting data {err}')
        return None


def save_todo(new_todo: str) -> bool:
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute(f"insert into todos (name, done) values ('{new_todo}', false);")
        con.commit()
        cur.close()
        con.close()
        print(f'Saved new todo to the database [{new_todo}]')
        return True
    except DBError as err:
        print(f'Error while inserting data{err}')
        return False
