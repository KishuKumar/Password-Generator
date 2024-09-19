import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def new_password():
    letters_num = random.randint(6, 8)
    digits_num = random.randint(2, 4)
    sym_num = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0, letters_num)]
    password_numbers = [random.choice(numbers) for _ in range(0, digits_num)]
    password_symbols = [random.choice(symbols) for _ in range(0, sym_num)]

    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)
    return password
