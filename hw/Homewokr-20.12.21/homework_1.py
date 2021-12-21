"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""
import sqlite3

def create_product_table():
    with sqlite3.connect("table_product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR,
               price INTEGER,
               amount INTEGER, 
               comment VARCHAR,
            );
            """,
        )
        session.commit()


def create_product(name: str, price: int, amount: int, comment: str):
    with sqlite3.connect("table_product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            f"""
            INSERT INTO user (name, price, amount, comment)
            VALUES (?, ?, ?, ?, );
            """,
            (name, price, amount, comment),
        )
        session.commit()


def update_product(name: str, price: int, amount: int, comment: str):
    with sqlite3.connect("table_product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            f"""
            UPDATE user
            SET firstname = "Roman"
            WHERE email = "manti.by@gmail.com";
        )
        session.commit()

create_product_table()