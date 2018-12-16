
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from instance.config import CONFIGS

env = os.getenv('FLASK_ENV')
url = CONFIGS[env].DATABASE_URI

class ReportDB():

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
    
    def create_tables(self): 
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS users(
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
        self.conn.commit()

    def save_to_db(self,query_string, tuple_data):
        self.cur.execute(query_string, tuple_data)
        self.conn.commit()

    def add_to_db(self, query_string, tuple_data):
        self.cur.execute(query_string, tuple_data)
        self.conn.commit()
        response = self.cur.fetchone()
        return response

    def get_one(self,query_string):
        self.cur.execute(query_string)
        return self.cur.fetchone()

    def get_all(self,query_string):
        self.cur.execute(query_string)
        return self.cur.fetchall()
    
    def update_table_row(self, query_string):
        resp = self.cur.execute(query_string)
        self.conn.commit()
    
    def delete(self, query_string):
        resp = self.cur.execute(query_string)
        self.conn.commit()
 
    def __del__(self):
        self.conn.close()
    
    def drop_table(self):
        self.cur.execute("""
            DROP TABLE IF EXISTS users CASCADE;\
            DROP TABLE IF EXISTS reports CASCADE;""")
        self.conn.commit()








