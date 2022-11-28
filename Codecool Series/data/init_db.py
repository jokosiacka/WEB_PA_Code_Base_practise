from data_manager import get_connection_data, establish_connection
import os


def init_db():
    init_conn = get_connection_data('postgres')
    db_name = os.environ.get('MY_PSQL_DBNAME')

    with establish_connection(connection_data=init_conn) as conn:
        with conn.cursor() as cursor:
            try:
                drop_statement = 'DROP DATABASE IF EXISTS "{}";'.format(db_name)
                create_statement = 'CREATE DATABASE "{}";'.format(db_name)
                cursor.execute(drop_statement)
                cursor.execute(create_statement)
                print("Database created")
            except Exception as ex:
                print("Database creation failed")
                print(ex.args)


def create_schema():
    creation_script_file = 'data/db_schema/01_create_schema.sql'
    with open(creation_script_file) as schema_script:
        with establish_connection() as conn, \
                conn.cursor() as cursor:
            try:
                sql_to_run = schema_script.read()
                cursor.execute(sql_to_run)
                print("Database schema created")
            except Exception as ex:
                print("Schema creation failed")
                print(ex.args)
