from kassa.utils import get_change

price = input("Введите стоимость товара: ").strip()
paid = input("Введите купюры внесенные в кассу: ").strip()
print(get_change(price, paid))