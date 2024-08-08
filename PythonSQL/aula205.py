# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
from tkinter import CURRENT
import pymysql
import pymysql.cursors
import dotenv
import os
from typing import cast

TABLE_NAME = 'users'
CURRENT_CURSOR = pymysql.cursors.SSDictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES ' 
            '(%s, %s) '
        )
        data = ('Mauricio', 23)
        result = cursor.execute(sql, data)
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES ' 
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "name": "Mario",
            "age": 25,
        }
        result = cursor.execute(sql, data2)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES ' 
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Maria", "age": 30},
            {"name": "João", "age": 35},
            {"name": "Luis","age": 25,},
            )
        result = cursor.executemany(sql, data3)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES ' 
            '(%s, %s) '
        )
        data4 = (
            ("Lucas", 28),
            ("Pedro", 32)
            )
        result = cursor.executemany(sql, data4)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # id_recived = input('Type id: ')
        # column = 'id'
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id = 5 '
            # 'WHERE id BETWEEN %s AND %s  '
            )
        cursor.execute(sql)
        # cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        # print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
        data5 = cursor.fetchall()
        
        # for row in data5:
        #     print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '

        )
        cursor.execute(sql, (1, ))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        # data6 = cursor.fetchall()

        # for row in cursor.fetchall():
        #     print(row)

    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name = %s, age = %s '
            'WHERE id = %s '

        )
        cursor.execute(sql, ('Eleonor', 34, 4))
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
 
        data6 = cursor.fetchall()

        for row in data6:
            print(row)

        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)
    connection.commit()