from intity.store import Store
from intity.shop import Shop
from intity.request import Request

store = Store(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1,
    }
)

shop = Shop(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1,
    }
)

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nДобрый день!\n')

    while True:

        # TODO: Вывести содержимое складов:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}: \n {storages[storage_name].get_items()}')

        user_input = input('Введите запрос в формате "Доставить 3 печеньки из склада в магазин"\n'
                           'Введите "стоп" или "stop", если хотите закончить:\n'
                           )
        if user_input.lower() in ('stop', 'стоп'):
            break

        # TODO: Провалидировать пункты отправки и значений
        request = Request(request=user_input, storages=storages)

        # TODO: запустить доставку
        if storages[request.departure].remove(request.product, request.amount):
            print(f'Курьер забрал {request.product} {request.amount} из {request.departure}')

            if storages[request.destination].add(request.product, request.amount):
                print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
            else:
                storages[request.departure].add(request.product, request.amount)
                print(f'Курьер вернул {request.amount} {request.product} в {request.departure}')

if __name__ == '__main__':
    main()
