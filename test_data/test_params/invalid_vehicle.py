from test_data.vehicles import Vehicles
from faker import Faker


class InvalidVehicle:
    @staticmethod
    def list_of_invalid_vehicle_parameters():
        fake = Faker('ru_RU')
        return [
            {
                'name': 'Создание ТС типа фургон без марки',
                'allureID': '39710',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MODEL_VEHICLE: '65207',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.PAYLOAD: '10',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа фургон без вместимости паллет',
                'allureID': '58012',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '65207',
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.PAYLOAD: '10',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа фургон без вместимости м куб',
                'allureID': '58013',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '65207',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.PAYLOAD: '10',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа фургон без грузоподъемности',
                'allureID': '39712',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '65207',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа фургон без госномера',
                'allureID': '58017',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_VAN,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_KAMAZ,
                Vehicles.MODEL_VEHICLE: '65207',
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_10,
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.PAYLOAD: '10',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа тягач без марки',
                'allureID': '39714',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_TRUCK,
                Vehicles.MODEL_VEHICLE: 'FH-TRUCK 6x4',
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа тягач без госномера',
                'allureID': '39716',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_TRUCK,
                Vehicles.MARK_VEHICLE: Vehicles.MARK_VEHICLE_VOLVO,
                Vehicles.MODEL_VEHICLE: 'FH-TRUCK 6x4',
                Vehicles.OWNERSHIP_TYPE: Vehicles.OWNERSHIP_TYPE_OWNED,
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа полуприцеп без вместимости паллет',
                'allureID': '58014',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.PAYLOAD: '15',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа полуприцеп без вместимости м куб',
                'allureID': '58015',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.PAYLOAD: '15',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа полуприцеп без грузоподъемности',
                'allureID': '39717',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                Vehicles.NUMBER: fake.bothify('?###??##').upper(),
                'error': 'Поле обязательно для заполнения.'
            },
            {
                'name': 'Создание ТС типа полуприцеп без госномера',
                'allureID': '58016',
                Vehicles.TYPE_VEHICLE: Vehicles.TYPE_VEHICLE_SEMITRAILER,
                Vehicles.PALLET_CAPACITY: Vehicles.PALLET_CAPACITY_40,
                Vehicles.CAPACITY_VOLUME: '18',
                Vehicles.PAYLOAD: '15',
                Vehicles.BODY_TYPE: Vehicles.BODY_TYPE_TENT,
                'error': 'Поле обязательно для заполнения.'
            },]
