
import os
import psycopg2
from psycopg2.extras import RealDictCursor
#local import
from instance.config import CONFIGS

env = os.getenv('FLASK_ENV')
url = CONFIGS[env].DATABASE_URI

class ReportDB():
    """
        Class for the methods of handling the database
    """
    def __init__(self):
    """
        Method for instatiating the class
    """
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
    
    def create_tables(self):
    """
        Method for creating new tables in the database
    """ 
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
    """
        Method for saving inputs to the database
    """
        self.cur.execute(query_string, tuple_data)
        self.conn.commit()

    def add_to_db(self, query_string, tuple_data):
    """
        Method for adding inputs to the database
    """
        self.cur.execute(query_string, tuple_data)
        self.conn.commit()
        response = self.cur.fetchone()
        return response

    def get_one(self,query_string):
    """
        Method for retrieving a single item from the database
    """
        self.cur.execute(query_string)
        return self.cur.fetchone()

    def get_all(self,query_string):
    """
        Method for retrieving all items of a table from the database
    """
        self.cur.execute(query_string)
        return self.cur.fetchall()
    
    def update_table_row(self, query_string):
    """
        Method for updating a specific row in the tables
    """
        resp = self.cur.execute(query_string)
        self.conn.commit()
    
    def delete(self, query_string):
    """
        Method for deleting a specific row from the tables
    """
        resp = self.cur.execute(query_string)
        self.conn.commit()
 
    def __del__(self):
        self.conn.close()
    
    def drop_table(self):
    """
        Method for destroying the tables after a test is complete
    """
        self.cur.execute("""
            DROP TABLE IF EXISTS users CASCADE;\
            DROP TABLE IF EXISTS reports CASCADE;""")
        self.conn.commit()








