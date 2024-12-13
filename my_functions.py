import random

def add(values) -> float:
    neg_numbers = [value for value in values if value < 0]
    return sum(neg_numbers)

def subtract(values) -> float:
    pos_numbers = [value for value in values if value > 0]
    if not pos_numbers:
        return 0
    difference = pos_numbers[0]
    for value in pos_numbers[1:]:
        difference -= value
    return difference

def multiply(values) -> float:
    if not values: 
        return 0
    product = 1
    for value in values:
        product *= value
    return product

def divide(values) -> float:
    if not values:
        raise ValueError("No values provided.")
    result = values[0]
    for value in values[1:]:
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= value
    return result

def choose(values) -> float:
    if not values:
        raise ValueError("No values provided.")
    return random.choice(values)