from intity.base_storages import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> bool:
        if name not in self.get_items() and self.get_unique_items_count() >= 5:
            print('Cлишком много разных товаров')
            return False

        return super().add(name, amount)
