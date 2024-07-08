def check_name(name):
    if len(name) < 1 or any(char.isdigit() for char in name):
        return False
    return True

def validate_id(id):
    id_12_digits = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    if id is None or len(id) != 9 or not id.isdigit():
        return False
    id = id.zfill(9)
    sum_digits = sum((int(id[i]) * id_12_digits[i] % 10 + int(id[i]) * id_12_digits[i] // 10) for i in range(9))
    return sum_digits % 10 == 0

def check_password(pass1, pass2):
    return pass1 == pass2

def check_phone(number):
    return len(number) == 10 and number.isdigit()

def check_correct(name):
    special_chars = "!@#$%^&*().,/+-='"
    return not any(char in special_chars for char in name)

def validate_name(name):
    return len(name) > 2 and name.isalpha()
