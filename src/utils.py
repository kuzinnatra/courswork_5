import requests
import psycopg2
from typing import Any

employer_ids = [9694561, 4219, 5919632, 5667343, 9301808, 774144, 10571093, 198614, 6062708, 4306]


def get_employee_data():
    """
    функция для получения данных о компаниях с сайта HH.ru
    """
    employers = []
    for employer_id in employer_ids:
        url_emp = f"https://api.hh.ru/employers/{employer_id}"
        employer_info = requests.get(url_emp, ).json()
        employers.append(employer_info)

    return employers


def get_vacancies_data():
    """
    функция для получения данных о вакансиях с сайта HH.ru
    """
    vacancy = []
    for vacacies_id in employer_ids:
        url_vac = f"https://api.hh.ru/vacancies?employer_id={vacacies_id}"
        vacancy_info = requests.get(url_vac, params={'page': 0, 'per_page': 100}).json()
        vacancy.extend(vacancy_info['items'])
    return vacancy


def create_database(database_name: str, params: dict) -> None:
    """
    функция для создания Базы Данных и создания таблиц в БД
    """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE IF EXISTS {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                employer_id INTEGER,
                employer_name text not null,
                employer_area TEXT not null,
                url TEXT,
                open_vacancies INTEGER
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancy (
                vacancy_id INTEGER,
                vacancy_name VARCHAR,
                vacancy_area VARCHAR,
                salary INTEGER,
                employer_id INTEGER,
                vacancy_url VARCHAR
            )
        """)

    conn.commit()
    conn.close()