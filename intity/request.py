from intity.abstract_storage import AbstractStorages
from typing import Dict


class Request:
    def __init(self, request: str, storages: Dict[str, AbstractStorages]):
        # TODO: Разделить строку по пробелам
        parsed_request = request.lower().split(' ')
        if len(parsed_request) != 7:
            print('Неправильный запрос')
            return False

        # TODO: вывести значения из строки в атрибуты класса
        self.amount = int(parsed_request[1])
        self.product = (parsed_request[2])
        self.departure = (parsed_request[4])
        self.destination = (parsed_request[6])

        # TODO: Провалидировать пункты отправки и значений
        if self.departure not in storages or self.destination not in storages:
            print('Неизвестный склад')
            return

