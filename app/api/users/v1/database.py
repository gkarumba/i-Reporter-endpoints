
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from instance.config import CONFIGS

env = os.getenv('FLASK_ENV')
url = CONFIGS[env].DATABASE_URI

class ReportDB():
    @classmethod
    def start_db(cls,url):
        cls.conn = psycopg2.connect(url)
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)
    
    @classmethod
    def create_tables(cls): 
        cls.cur.execute(""" CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(5000) NOT NULL, 
        firstname VARCHAR(50) NOT NULL,
        lastname  VARCHAR(50) NOT NULL,
        phonenumber INTEGER NOT NULL,
        isAdmin BOOLEAN default False
        );
        CREATE TABLE IF NOT EXISTS reports(
        report_id SERIAL PRIMARY KEY,
        createdBy INT NOT NULL REFERENCES users(user_id),
        createdOn VARCHAR(350) default current_timestamp,
        flag_type VARCHAR(24) NOT NULL,
        location VARCHAR(30) NOT NULL,
        status VARCHAR (24) default 'Draft',
        comments VARCHAR (500) NOT NULL
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







