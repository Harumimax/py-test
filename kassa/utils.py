nominals = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
nominals = sorted(nominals, reverse=1)

def get_change(price, paid):
    price = float(price)
    list_paid = paid.split(" ")
    float_list_paid = [float(j) for j in list_paid]
    full_paid = sum(float_list_paid)
    #print(f"Это полная цена {full_paid}")
    if full_paid < price:
        raise ValueError("Дано мало денег")
    change = full_paid - price
    print(f"Это сдача {change}")
    result = []
    for i in nominals:
        #print(f"Это i в фор {i}")
        if change // i > 0:
            diff = change // i
            #print(f"Это i {i}")
            #print(f"Это diff {diff}")
            for o in range(int(diff)):
                result.append(i)
            #print(f"Это результат {result}")
            change = change - diff * i
    #print(result)
    result = " ".join([str(a) for a in result])
    return result

if __name__ == "__main__":
    price = input("Введите стоимость товара: ").strip()
    paid = input("Введите купюры внесенные в кассу: ").strip()
    print(get_change(price, paid))