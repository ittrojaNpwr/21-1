
from intity.abstract_storage import AbstractStorages


class BaseStorage(AbstractStorages):
    def __init__(self, items: dict, capacity: int = 100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> bool:
        if self.get_unique_items_count() >= 5:
            print('Cлишком много разных товаров')
            return

        # TODO: Проверить что места достаточно
        if self.get_free_space() < amount:
            print('Не хватает места')
            return False

        # TODO: Добавить товар
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

        return True

    def remove(self, name: str, amount: int) -> bool:
        # TODO: Проверить есть ли такой товар и хватает ли места для него
        if name not in self.__items:
            print('Такого товар нет')
            return False
        if self.__items[name] < amount:
            print('Недостаточно товара')
            return False

        # TODO: Вычесть необходимое кол-во товара, если товара станет 0 - удалить товар из списка
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

        return True

    def get_free_space(self) -> int:
        # TODO: Посчитать сумму значений в словаре __items. Вычесть ее из __capacity
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
