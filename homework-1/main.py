"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

import csv
import datetime


def insert_into_table_customers():
    '''Функция открывает файл и заполняет данными таблицу customers'''

    with psycopg2.connect(host="localhost", database="north", user="postgres", password="12345") as conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    customer_id = row["customer_id"]
                    company_name = row["company_name"]
                    contact_name = row["contact_name"]
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id,
                                                                              company_name,
                                                                              contact_name))
                    cur.execute('SELECT * FROM customers')
                    conn.commit()

                    rows = cur.fetchall()

                    for row in rows:
                        print(row)
        conn.close()


def insert_into_table_employees():
    '''Функция открывает файл и заполняет данными таблицу employees'''

    with psycopg2.connect(host="localhost", database="north", user="postgres", password="12345") as conn:
        with conn.cursor() as cur:
            with open('north_data/employees_data.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    employee_id = row["employee_id"]
                    first_name = row["first_name"]
                    last_name = row["last_name"]
                    title = row["title"]
                    birth_date = row["birth_date"]
                    notes = row["notes"]
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s)', (
                        int(employee_id),
                        str(first_name),
                        str(last_name),
                        str(title),
                        datetime.datetime.strptime(birth_date, '%Y-%m-%d'),
                        str(notes)))
                    cur.execute('SELECT * FROM customers')
                    conn.commit()

                    rows = cur.fetchall()

                    for row in rows:
                        print(row)
        conn.close()


def insert_into_table_orders():
    '''Функция открывает файл и заполняет данными таблицу orders'''

    with psycopg2.connect(host="localhost", database="north", user="postgres", password="12345") as conn:
        with conn.cursor() as cur:
            with open('north_data/orders_data.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    order_id = row["order_id"]
                    customer_id = row["customer_id"]
                    employee_id = row["employee_id"]
                    order_date = row["order_date"]
                    ship_city = row["ship_city"]
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s, %s, %s)', (
                        int(order_id),
                        str(customer_id),
                        int(employee_id),
                        datetime.datetime.strptime(order_date, '%Y-%m-%d'),
                        str(ship_city)))
                    cur.execute('SELECT * FROM customers')
                    conn.commit()

                    rows = cur.fetchall()

                    for row in rows:
                        print(row)
        conn.close()

insert_into_table_orders()

