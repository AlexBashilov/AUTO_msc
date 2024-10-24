from dataclasses import dataclass


@dataclass
class Vehicles:
    TYPE_VEHICLE = 'Тип ТС'
    TYPE_VEHICLE_TRUCK = 'Тягач'
    TYPE_VEHICLE_SEMITRAILER = 'Полуприцеп'
    TYPE_VEHICLE_VAN = 'Фургон'
    MARK_VEHICLE = 'Марка ТС'
    MARK_VEHICLE_KAMAZ = 'KAMAZ'
    MARK_VEHICLE_VOLVO = 'VOLVO'
    MODEL_VEHICLE = 'Модель ТС'
    PALLET_CAPACITY = 'Вместимость палет'
    PALLET_CAPACITY_10 = '10'
    PALLET_CAPACITY_40 = '40'
    CAPACITY_CENTIMETERS = 'Вместимость м³'
    BODY_TYPE = 'Тип кузова'
    BODY_TYPE_TENT = 'Тент'
    OWNERSHIP_TYPE = 'Тип владения ТС'
    OWNERSHIP_TYPE_OWNED = 'В собственности'
    NUMBER = 'Гос. номер'
    PAYLOAD = 'Грузоподъемность, т'
