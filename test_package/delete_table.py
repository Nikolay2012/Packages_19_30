
def delete_table(cursor: object, name_table: str):
    try:
        cursor.execute(f"DROP TABLE {name_table}")
    except:
        print(f"Cannot be deleted table does not exist '{name_table}'")