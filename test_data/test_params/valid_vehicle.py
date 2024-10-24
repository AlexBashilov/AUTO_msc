from test_data.vehicles import Vehicles
from faker import Faker


class ValidVehicle:
    def list_of_vehicle_parameters(self):
        fake = Faker('ru_RU')
        return [
            {
                'name': 'фургон',
                'allureID': '35669',
                'allureIdExistVehicle': '49158',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '53215',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_CENTIMETERS: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                Vehicles.PAYLOAD: '10'
            },
            {
                'name': 'тягач',
                'allureID': '27611',
                'allureIdExistVehicle': '49159',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_TRUCK,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_VOLVO,
                Vehicles.MODEL_VEHICLE: 'FH-TRUCK 6x4',
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
            },
            {
                'name': 'полуприцеп',
                'allureID': '35668',
                'allureIdExistVehicle': '49160',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                Vehicles.PAYLOAD: '15'
            },
            {
                'name': 'фургон без модели',
                'allureID': '39711',
                'allureIdExistVehicle': '49161',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_CENTIMETERS: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                Vehicles.PAYLOAD: '10'
            },
            {
                'name': 'фургон без типа тента',
                'allureID': '39713',
                'allureIdExistVehicle': '49162',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '53215',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_CENTIMETERS: '18',
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                Vehicles.PAYLOAD: '10'
            },
            {
                'name': 'тягач без модели',
                'allureID': '39715',
                'allureIdExistVehicle': '49163',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_TRUCK,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_VOLVO,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
            },
            {
                'name': 'полуприцеп без типа кузова',
                'allureID': '39718',
                'allureIdExistVehicle': '37074',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                Vehicles.PAYLOAD: '105'
            },
        ]
