from enum import Enum


class FederalDistrict(str, Enum):
    """
    Список федеральных округов
    """

    CFO_DISTRICT = "ЦФО"
    PFO_DISTRICT = "ПФО"

    def __str__(self) -> str:
        return self.value
