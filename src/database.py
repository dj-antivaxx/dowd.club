import sqlite3


def get_db_connection():
    conn = sqlite3.connect('./artifacts/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_email_schema(connection):
    schema_email = """
    CREATE TABLE EMAILZ (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EMAIL TEXT NOT NULL,
        EMAILTIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """
    connection.executescript(schema_email)

def create_rsvp_schema(connection):
    schema_rsvp = """
    CREATE TABLE RSVP (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        REFERRAL TEXT NOT NULL,
        EMAIL TEXT NOT NULL
    );
    """
    connection.executescript(schema_rsvp)

def create_feedback_schema(connection):
    schema_feedback = """
    CREATE TABLE FEEDBACK (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FEEDBACK TEXT NOT NULL,
        FEEDBACKTIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """
    connection.executescript(schema_feedback)

def insert_to_rsvp_schema(name, referral, email):
    connection = get_db_connection()
    connection.execute("INSERT INTO RSVP VALUES (NULL, ?, ?, ?)", (name, referral, email))
    connection.commit()
    connection.close()

def insert_to_feedback_schema(feedback):
    connection = get_db_connection()
    connection.execute("INSERT INTO FEEDBACK VALUES (NULL, ?, CURRENT_TIMESTAMP)", (feedback, ))
    connection.commit()
    connection.close()

def insert_to_email_schema(email):
    connection = get_db_connection()
    connection.execute("INSERT INTO EMAILZ VALUES (NULL, ?, CURRENT_TIMESTAMP)", (email, ))
    connection.commit()
    connection.close()
