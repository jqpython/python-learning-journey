def coffee_calculator_order(menu, order):

    subtotal = 0;

    for item in order:
        subtotal = subtotal + menu[item]

    print("The total is: ", subtotal)

    tax = subtotal * 0.08 # tax formula
    print("The tax is: ", tax)
    total = subtotal + tax
    return round(total,2)

menu = {
       "coffee": 3.50,
       "muffin": 2.40,
       "sandwich": 4.40
}

order = ["coffee", "coffee", "muffin","sandwich"]

result = coffee_calculator_order(menu,order)
print ("The total amount with tax is", result)
