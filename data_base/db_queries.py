from typing import Text, List

from utils.db_connect import connection
from data_base.models.Items_db import ItemsDB
from data_base.models.vehicle_db import VehicleDB


class SqlQueries:
    def __init__(self, connect_db: connection):
        self.__connect_db = connect_db

    def __execute_request_select(self, request: Text) -> List:
        with self.__connect_db.cursor() as cursor:
            cursor.execute(request)
            columns = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()
            dict_result = [dict(zip(columns, row)) for row in result]
        return dict_result

    def __execute_request_update_insert_delete(self, request: Text) -> List | None:
        with self.__connect_db.cursor() as cursor:
            cursor.execute(request)
            self.__connect_db.commit()
            if cursor.description:
                result = cursor.fetchall()
                return result
            else:
                return None

    def insert_new_item(self, items: ItemsDB) -> int:
        request_insert = f"""INSERT INTO book_cost_items (item_name, guid, description)
        VALUES ('{items.item_name}', '{items.guid}', '{items.description}'
        ) RETURNING id"""
        return self.__execute_request_update_insert_delete(request_insert)[0][0]

    def get_all_items(self) -> List:
        request = f"""select * from book_cost_items"""
        return self.__execute_request_select(request)
    
    
    def get_driver_by_id(self, driver_id) -> List:
        request = f"""select * from driver where id ='{driver_id}'"""
        return self.__execute_request_select(request)


    def get_items_by_id(self, items: ItemsDB) -> List:
        request = f"""select * from book_cost_items where guid ='{items.guid}'"""
        return self.__execute_request_select(request)
    
    
    def get_tc_by_driver_id(self, driver_id) -> List:
        request = f"""select * from link_driver_vs_transport_company where driver_id ='{driver_id}'"""
        return self.__execute_request_select(request)

    def delete_driver_by_id(self, driver):
        request_delete_driver = f"""DELETE from driver WHERE id={driver}"""
        self.__execute_request_update_insert_delete(request_delete_driver)
        request_delete_link = (
            f"""DELETE from link_driver_vs_transport_company WHERE driver_id={driver}"""
        )
        self.__execute_request_update_insert_delete(request_delete_link)

    def insert_new_vehicle(self, vehicle: VehicleDB) -> int:
        request_insert = f"""INSERT INTO vehicle (vehicle_type_id, number, brand, model, vehicle_ownership_type_id, capacity_type_id, capacity_volume, cargo_body_type_id, weight_capacity, created_at, updated_at)
        VALUES ('{vehicle.vehicle_type_id}', '{vehicle.number}', '{vehicle.brand}', '{vehicle.model}', '{vehicle.vehicle_ownership_type_id}',
        '{vehicle.capacity_type_id}', '{vehicle.capacity_volume}', '{vehicle.cargo_body_type_id}', '{vehicle.weight_capacity}',
        '{vehicle.created_at}', '{vehicle.updated_at}') RETURNING id"""
        return self.__execute_request_update_insert_delete(request_insert)[0][0]

    def delete_vehicle_by_id(self, vehicle):
        request_delete = f"""DELETE from vehicle WHERE id={vehicle}"""
        self.__execute_request_update_insert_delete(request_delete)

    def get_trips_by_route_name(self, routeName) -> int:
        request = f"""select count(*) AS kolvo from route right join trip on route.id = trip.route_id where name ='{routeName}'"""
        return self.__execute_request_select(request)[0]["kolvo"]

    def get_routes_by_route_name(self, routeName) -> int:
        request = f"""select count(*) AS kolvo from route where name ='{routeName}'"""
        return self.__execute_request_select(request)[0]["kolvo"]

    def get_route_data_by_route_name(self, routeName) -> List:
        request = f"""select * from route where name ='{routeName}'"""
        return self.__execute_request_select(request)

    def get_route_point_by_route_id(self, route_id) -> int:
        request = f"""select * from route_point where route_id={route_id}"""
        return self.__execute_request_select(request)[0]["id"]

    def delete_route_operation_by_route_point_id(self, route_point_id):
        request = (
            f"""DELETE from route_operation WHERE route_point_id={route_point_id}"""
        )
        self.__execute_request_update_insert_delete(request)

    def delete_route_point_by_route_point_id(self, route_point_id):
        request = f"""DELETE from route_point WHERE id={route_point_id}"""
        self.__execute_request_update_insert_delete(request)

    def delete_route_point_by_route_id(self, route_id):
        request = f"""DELETE from route_point WHERE route_id={route_id}"""
        self.__execute_request_update_insert_delete(request)

    def delete_route_by_route_name(self, route_name):
        request = f"""DELETE from route WHERE name='{route_name}'"""
        self.__execute_request_update_insert_delete(request)
