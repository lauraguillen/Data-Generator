import random
import string


def generate_id():
    key_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return key_id


def generate_pesel(bday, sex):
    number = ""
    year = str(bday.year)[:-2]
    month = str(bday.month)
    day = str(bday.day)
    number.join(year + month + day)
    for i in range(11):
        number = number + str(random.randint(1, 9))
    return number
