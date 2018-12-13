
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class ReportDB():
    @classmethod
    def start_db(cls,URI):
        cls.conn = psycopg2.connect(URI)
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)
    
    @classmethod
    def create_tables(cls): 
        cls.cur.execute(""" CREATE TABLE users(
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL, 
        firstname VARCHAR(50) NOT NULL,
        lastname  VARCHAR(50) NOT NULL,
        phonenumber INTEGER NOT NULL
        );
        CREATE TABLE reports(
        report_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        flag_type VARCHAR(24) NOT NULL,
        location VARCHAR(30) NOT NULL,
        status VARCHAR (24) NOT NULL,
        comments VARCHAR (500) NOT NULL, 
        );""")
        cls.conn.commit()

    @classmethod
    def save_to_db(cls,query_string, tuple_data):
        cls.cur.execute(query_string, tuple_data)
        cls.conn.commit()

    @classmethod
    def add_to_db(cls, query_string, tuple_data):
        cls.cur.execute(query_string, tuple_data)
        cls.conn.commit()
        response = cls.cur.fetchone()
        return response

    @classmethod
    def get_one(cls,query_string):
        cls.cur.execute(query_string)
        return cls.cur.fetchone()

    @classmethod
    def get_all(cls,query_string):
        cls.cur.execute(query_string)
        return cls.cur.fetchall()
    
    @classmethod
    def update_table_row(cls, query_string):
        resp = cls.cur.execute(query_string)
        cls.conn.commit()
    
    @classmethod
    def delete(cls, query_string):
        resp = cls.cur.execute(query_string)
        cls.conn.commit()
    
    @classmethod
    def __del__(cls):
        cls.conn.close()
    
    @classmethod
    def drop_table(cls):
        cls.cur.execute("""
            DROP TABLE IF EXISTS users CASCADE;\
            DROP TABLE IF EXISTS reports CASCADE;""")
        cls.conn.commit()





