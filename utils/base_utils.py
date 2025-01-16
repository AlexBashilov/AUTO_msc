import re
from datetime import datetime, timedelta, timezone

from allure_commons._allure import step

@step("Сгенерировать дату в формате ISO")
def generate_date_as_string_iso(add_day=0, hour=0, new_timezone=0) -> str:
    return (
        (datetime.now() + timedelta(days=add_day))
        .replace(
            hour=hour,
            minute=0,
            second=0,
            microsecond=0,
            tzinfo=timezone(timedelta(hours=new_timezone)),
        )
        .isoformat()
    )

@step("Преобразовать значение None в пустую строку")
def none_to_empty_string(value):
    return value if value is not None else ""

@step("Объединить массив словарей в один словарь")
def combined_dict_with_list(list_of_dicts: list[dict]):
    combined_dict = {}

    for d in list_of_dicts:
        for key, value in d.items():
            if key not in combined_dict:
                combined_dict[key] = []
            combined_dict[key].append(value)

    return combined_dict

@step("Удалить спецсимволы из строки, пробелы в начале и конце строки и привести символы к верхнему регистру")
def clean_and_transform_string(input_string: str) -> str:
    trimmed_string = input_string.strip()
    alphanumeric_string = re.sub(r'[^a-zA-Z0-9а-яА-Я]', '', trimmed_string)
    result_string = alphanumeric_string.upper()

    return result_string