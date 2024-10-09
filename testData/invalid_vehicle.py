from testData.vehicles import Vehicles
from faker import Faker


class InvalidVehicle:
    def list_of_invalid_vehicle_parameters(self):
        fake = Faker('ru_RU')
        return [
            {
                'name': 'Создание ТС типа фургон без марки',
                'allureID': '39710',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MODEL_VEHICLE: '53215',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_CENTIMETERS: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##'),
                Vehicles.PAYLOAD: '10',
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа фургон без госномера',
                'allureID': '39712',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '53215',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_CENTIMETERS: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.PAYLOAD: '10',
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа фургон без грузоподъемности',
                'allureID': '39712',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '53215',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_CENTIMETERS: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##'),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа тягач без марки',
                'allureID': '39714',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_TRUCK,
                Vehicles.MODEL_VEHICLE: 'FH-TRUCK 6x4',
                Vehicles.NUMBER: fake.bothify('?###??##'),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа тягач без госномера',
                'allureID': '39716',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_TRUCK,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_VOLVO,
                Vehicles.MODEL_VEHICLE: 'FH-TRUCK 6x4',
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа полуприцеп без госномера',
                'allureID': '39717',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.PAYLOAD: '10',
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа полуприцеп без грузоподъемности',
                'allureID': '39717',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##'),
                'error': 'Поле обязательно для заполнения.'
            }, ]
