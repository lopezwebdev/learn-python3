#calls chatbot only once when the order is completed

def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

def get_drink_type():
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()       
    else:
        print_message()
        return get_drink_type()

def order_latte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")

    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

def get_temperature():
    res = input("Would you like your drink hot or iced? \n[a] Hot \n[b] Iced \n> ")
    
    if res == 'a':
        return "hot"
    elif res == 'b':
        return "iced"
    else:
        print_message()
        return get_temperature()

def coffee_bot():
    print("Welcome to the Cafe!")
    size = get_size()
    drink_type = get_drink_type()
    temperature = get_temperature()
    print("Alright, that's a {} {} {}!".format(size, temperature, drink_type))

    name = input("Can I get your name please? \n> ")
    print("Thanks, {}! Your drink will be ready shortly.".format(name))

# Call coffee_bot()!
coffee_bot()
