from enum import Enum


class ShopList(str, Enum):
    """
    Список магазинов и складов
    """

    MSK_DOMODEDOVO_WAREHOUSE = "МСК - Склад Домодедово"
    NN_DOSKINO_WAREHOUSE = "НН - Доскино Склад"
    SPB_WAREHOUSE = "СПБ - РЦ Шушары Бадаевское"
    MRK_WAREHOUSE = "МРК - Мурманск Магазин-склад"
    MRK_ATLANTIC_SHOP = "МРК - Мурманск Атлантика Магазин"
    MSK_BAGRATION_SHOP = "МСК - Багратионовская Магазин"
    MSK_VIDNOE_SHOP = "МСК - Видное Магазин"
    MSK_KUBINKA_SHOP = "МСК - Кубинка ПВЗ"
    MSK_SEVASTOPOL_SHOP = "МСК - Севастопольский Магазин"
    KAZAN_WAREHOUSE = "КАЗ - Казань Склад"
    KVR_LENINA_SHOP = "КВР - Ковров Ленина Магазин"
    KIR_GORKOGO_SHOP = "КИР - Киров Горького Магазин"
    KIR_PROFSOUZE_SHOP = "КИР - Киров Профсоюзная Магазин"
    KIR_MOSCOW_SHOP = "КИР - Киров Московская Магазин"
    KIR_POPOVA_SHOP = "КИР - Киров Попова Магазин"
    KIR_KOLCOVA_SHOP = "КИР - Киров Кольцова Магазин"
    KIR_MIXEEVA_SHOP = "КИР - Киров Михеева Магазин"
    KIR_WORCA_SHOP = "КИР - Киров Щорса Магазин"
    KIR_SOVETSKAYA_SHOP = "КИР - Киров Советская Магазин"
    PERM_WAREHOUSE = "ПЕР - Пермь Стахановская Магазин-склад"
    PERM_UINSKAYA_SHOP = "ПЕР - Пермь Уинская Магазин"
    PERM_OVERYATSKAYA_SHOP = "ПЕР - Пермь Оверятская Магазин"
    PERM_LASVINSKAYA_SHOP = "ПЕР - Пермь Ласьвинская Магазин"
    SPB_BEGOVAYA = "СПБ - Беговая ПВЗ"

    def __str__(self) -> str:
        return self.value
