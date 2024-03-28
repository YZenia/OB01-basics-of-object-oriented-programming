class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
# Создание магазинов
scooter_store = Store("Двигатель", "Деревня поставщик 2.5.7")
electric_transport_store = Store("Электро Транспорт", "Город поставщик 3.4.8")
motoblock_store = Store("Мотоблоки", "Поселок поставщик 5.6.9")

# Добавление товаров в магазины
scooter_store.add_item("Sport Champ", 99000)
scooter_store.add_item("Vento City Elegance", 170000)
# Добавьте остальные товары аналогичным образом...
# Тестирование методов
print(f"Цена Sport Champ в магазине {scooter_store.name}: {scooter_store.get_item_price('Sport Champ')}")
scooter_store.update_item_price("Sport Champ", 95000)
print(f"Новая цена Sport Champ в магазине {scooter_store.name}: {scooter_store.get_item_price('Sport Champ')}")
scooter_store.remove_item("Sport Champ")
print(f"Цена Sport Champ в магазине {scooter_store.name} после удаления: {scooter_store.get_item_price('Sport Champ')}")
