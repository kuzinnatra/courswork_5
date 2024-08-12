from src.utils import (get_employee_data, create_database, save_data_to_database_emp, save_data_to_database_vac,
                   get_vacancies_data)
from config import config
from src.DBManager import DBManager


def main():
    params = config()

    data_emp = get_employee_data()
    data_vac = get_vacancies_data()
    create_database('hh', params)
    save_data_to_database_emp(data_emp, 'hh', params)
    save_data_to_database_vac(data_vac, 'hh', params)
    db_manager = DBManager(params)
    print(f"Выберите запрос: \n"
          f"1 - Список всех компаний и количество вакансий у каждой компании\n"
          f"2 - Cписок всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
          f"3 - Средняя зарплата по вакансиям\n"
          f"4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
          f"5 - Список всех вакансий, в названии которых содержатся запрашиваемое слово\n"
          f"0 - Выход из программы")



    while True:
        user_input = input('\nВведите номер запроса:\n')
        if user_input == "1":
            companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний и количество вакансий у каждой компании:")
            for i in companies_and_vacancies_count:
                print(i)

        elif user_input == "2":
            all_vacancies = db_manager.get_all_vacancies()
            print("Cписок всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию:")
            for i in all_vacancies:
                print(i)

        elif user_input == '3':
            avg_salary = db_manager.get_avg_salary()
            print("Средняя зарплата по вакансиям:")
            for i in avg_salary:
                print(i)

        elif user_input == "4":
            vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
            print("Список всех вакансий, у которых зарплата выше средней по всем вакансиям:")
            for i in vacancies_with_higher_salary:
                print(i)

        elif user_input == "5":
            user_input = input('Введите ключевое слово ')
            vacancies_with_keyword = db_manager.get_vacancies_with_keyword(user_input)
            print("Список всех вакансий, в названии которых содержатся запрашиваемое слово:")
            for i in vacancies_with_keyword:
                print(i)

        elif user_input == '0':
            break


if __name__ == '__main__':
    main()