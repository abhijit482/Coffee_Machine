import os

#clear()

#game Data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#if coin enough or more will call make coffee func
def process_coins(selection):
    global profit
    print('''
    Enter quater: 
    Enter Dimes: 
    Enter nickles:
    Enter penies:
    ''')
    quarters = int(input("Enter quater: "))
    clear = lambda: os.system('cls')
    clear()
    print(f'''
        Enter quater: {quarters} No.s
        Enter Dimes: 
        Enter nickles:
        Enter penies:
        ''')
    dimes = int(input("Enter Dimes: "))
    clear = lambda: os.system('cls')
    clear()
    print(f'''
            Enter quater: {quarters} No.s
            Enter Dimes: {dimes} No.s
            Enter nickles:
            Enter penies:
            ''')
    nickles = int(input("Enter nickles:"))
    clear = lambda: os.system('cls')
    clear()
    print(f'''
            Enter quater: {quarters} No.s
            Enter Dimes: {dimes} No.s
            Enter nickles: {nickles} No.s
            Enter penies:
            ''')
    pennies = int(input("Enter penies:"))
    clear = lambda: os.system('cls')
    clear()
    print(f'''
            Enter quater: {quarters} No.s
            Enter Dimes: {dimes} No.s
            Enter nickles: {nickles} No.s
            Enter penies: {pennies} No.s
            ''')
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

    if MENU[selection]["cost"]>total:
        print(f"Your total: ${total} is insufficient,Money Refunded")
    else:
        if total == MENU[selection]["cost"]:
          print(f"Your total coins: ${total} and coffee cost:{MENU[selection]["cost"]} ")
          profit += total
          make_coffe(selection)
        if total>MENU[selection]["cost"]:
            a = (total)-(MENU[selection]["cost"])
            print(f'''Your Total coins: ${total} and coffee cost:{MENU[selection]["cost"]} \nChange: ${round(a,2)}''')
            profit += MENU[selection]["cost"]
            make_coffe(selection)

def check_resource(type):
    flag = True
    load = dict(MENU[type]["ingredients"])
    #print(load)
    for item in load:
        if resources[item]<load[item]:
            print(f"Sorry insufficient {item}")
            flag = False

    return flag


def make_coffe(selection):
    requirement = dict(MENU[selection]["ingredients"])
    for item in requirement:
      resources[item] =  resources[item] - requirement[item]
    print(f"“Here is your {selection}. Enjoy!”.")



def prompt_exe(entry):
    global off
    if entry == 'espresso':
        # print('espresso')
        if check_resource(entry):
            process_coins(entry)
    elif entry == 'latte':
        # print('latte')
        if check_resource(entry):
            process_coins(entry)
    elif entry == 'capaccino':
        # print('capaccino')
        if check_resource(entry):
            process_coins(entry)
    elif entry == 'off':
        off = True
    elif entry == 'report':
        print(f'''
                  Water : {resources["water"]} ml
                  Milk  : {resources["milk"]} ml
                  Coffee: {resources["coffee"]} g
                  money : ${profit}''')
    else:
        print('Enter a proper choice: ')

off = False
while off == False:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    prompt_exe(prompt)

    