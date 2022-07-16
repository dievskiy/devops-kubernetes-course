#!/usr/bin/env python3.10

import psycopg2
from config import Config


def _get_db_connection():
    conn = psycopg2.connect(host=Config.HOST,
                            database=Config.POSTGRES_DB,
                            user=Config.POSTGRES_USER,
                            password=Config.POSTGRES_PASSWORD)
    return conn


def init_db():
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute(
            f'create table pongs (id SERIAL PRIMARY KEY not null, number int not null); insert into pongs (number) values (0);')
        con.commit()
        con.close()
    except Exception:
        print('Table already exists')


def inc_counter() -> int:
    """Increment counter and return an updated value"""
    counter = get_counter()
    counter += 1
    _save_count_to_db(counter)
    return counter


def get_counter() -> int:
    con = _get_db_connection()
    cur = con.cursor()
    cur.execute('select * from pongs where id = 1;')
    number = cur.fetchall()
    cur.close()
    con.close()
    return number[0][1]


def _save_count_to_db(count: int) -> None:
    con = _get_db_connection()
    cur = con.cursor()
    cur.execute(f'update pongs set number = {count} where id = 1;')
    con.commit()
    cur.close()
    con.close()
