from datetime import datetime


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True

def get_next_prime_year(birth_year):
    current_year = datetime.now().year
    
    age = current_year - birth_year
    next_prime_year = current_year

    while True:
        age += 1
        next_prime_year += 1
        
        if is_prime(age):
            break

    return next_prime_year
