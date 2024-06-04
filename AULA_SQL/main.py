import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(f"DELETE FROM {TABLE_NAME}")
# cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
# conn.commit()

# Delete mais cuidadoso
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

conn.commit()

# Cria a tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
conn.commit()

# Registrar valores nas colunas da tabela
# Cuidado: sql injection
sql = f"INSERT INTO {TABLE_NAME} " "(name, weight) " "VALUES " "(:name, :weight)"

# cursor.execute(sql, ["Jhon", 4])
# cursor.executemany(sql, [["Jhon", 4], ["Joana", 5]])
cursor.execute(sql, {"name": "Lucas", "weight": 5})
cursor.executemany(
    sql,
    [
        {"name": "Joao", "weight": 3},
        {"name": "Larissa", "weight": 7},
        {"name": "Joana", "weight": 8},
        {"name": "Luiz", "weight": 4},
    ],
)

conn.commit()


if __name__ == "__main__":
    print(sql)

    cursor.execute(f"DELETE FROM {TABLE_NAME} " 'WHERE id = "3"')
    cursor.execute(f"DELETE FROM {TABLE_NAME} " "WHERE id = 1")

    conn.commit()

    cursor.execute(f"UPDATE {TABLE_NAME} " "SET name='QUALQUER' " "WHERE id = 1")

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    conn.close()
