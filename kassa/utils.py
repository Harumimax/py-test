nominal = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}

def get_change(price, paid):
    price = float(price)
    list_paid = paid.split(" ")
    float_list_paid = [float(i) for i in list_paid]
    return float_list_paid

if __name__ == "__main__":
    price = input("Введите стоимость товара: ").strip()
    paid = input("Введите купюры внесенные в кассу: ").strip()
    print(get_change(price, paid))