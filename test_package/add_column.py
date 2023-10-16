 
def add_column(cursor: object, name_table: str, name_column: str, type_column: str):
    try:
        cursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}")
    except:
        print(f"Trying to create a duplicate column '{name_column}'")