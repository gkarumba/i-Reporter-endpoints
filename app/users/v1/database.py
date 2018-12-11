
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class ReportDB():
    def __init__(self):
        conn_string = "host='localhost' dbname='test_reporter' user='karumba' password='123456'"
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_tables(self): 
        self.cur.execute(""" CREATE TABLE users(
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
        return resp

    def delete(self, query_string):
        resp = self.cur.execut(query_string)
        self.conn.commit()
        return resp
    
    def __del__(self):
        self.conn.close()
    
    def drop_table(self):
        self.cur.execute("""
            DROP TABLE IF EXISTS users CASCADE;\
            DROP TABLE IF EXISTS reports CASCADE;""")
        self.conn.commit()





