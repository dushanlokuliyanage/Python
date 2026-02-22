

def calTotal(price : int , quntity: int, discount):
    sub = quntity *  price
    disTotal = sub * (100 - discount) / 100
    return disTotal

total = calTotal(500 , 5, 20)
print(total)