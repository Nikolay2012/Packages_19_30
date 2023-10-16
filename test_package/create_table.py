def create_table(cursor: object, name_table: str):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table} (ID INTEGER PRIMARY KEY)")