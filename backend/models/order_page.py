from backend.database import query_database

def load_result(data):
    sql_table = query_database.create_table()
    query_database.insert_table(sql_table)
    print("=============")
    print("load result")