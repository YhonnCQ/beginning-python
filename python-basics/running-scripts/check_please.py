import math


def split_check(total_bill, total_people):
    if total_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total_bill / total_people)


try:
    total_due = float(input("What is the total?   "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))
