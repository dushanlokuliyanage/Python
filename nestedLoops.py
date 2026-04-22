while True:
    materials = {
        "cement": 4000,
        "soil": 20000,
        "steelBar": 1500,
        "wire": 8000,
        "paint": 24000,
    }

    things = input("what do you want: ")
    q = int(input("Quantity: "))

    if things in materials:
        clau = materials[things] * q
        print("Total cost:", clau)

        if clau <= 10000:
            discount = clau * 0.05
            final_cost = clau - discount
            print(f"Discount (5%): {discount}")
            print(f"Final cost: {final_cost}")
