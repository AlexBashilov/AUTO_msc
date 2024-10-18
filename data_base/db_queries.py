from typing import Text, List
import allure
from utils.db_connect import connection
from data_base.models.drivers_db import DriversDB


class SqlQueries:
    def __init__(self, connect_db: connection):
        self.__connect_db = connect_db

    @allure.step("Выполнить sql запрос SELECT")
    def __execute_request_select(self, request: Text) -> List:
        with self.__connect_db.cursor() as cursor:
            cursor.execute(request)
            result = cursor.fetchall()
        return result

    @allure.step("Выполнить sql запрос UPDATE/INSERT/DELETE")
    def __execute_request_update_insert_delete(self, request: Text) -> None:
        with self.__connect_db.cursor() as cursor:
            cursor.execute(request)
            self.__connect_db.commit()

    @allure.step("Создать нового водителя в таблице driver")
    def insert_new_driver(self, driver: DriversDB):
        request_insert = f"""INSERT INTO driver (surname, name, patronymic, phone_number, passport_full_number, passport_date, state, created_at, license_number) 
        VALUES ('{driver.surname}', '{driver.name}', '{driver.patronymic}', '{driver.phone_number}', '{driver.passport_full_number}', '{driver.passport_date}', '{driver.state}', '{driver.created_at}', '{driver.license_number}')"""
        self.__execute_request_update_insert_delete(request_insert)
