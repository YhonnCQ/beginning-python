SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100


#   Create the calculate_price function. It takes number of tickets and
#   returns num_tickets * TICKET_PRICE
def calculate_price(num_of_tickets):
    #   Create a new constant for the 2 dollar service charge
    #   Add the service charge to our result
    return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


#   Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    #   Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))
    #   Gather the user's name and assign it to a new variable
    name = input("What is your name?    ")
    #   Prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}?   ".format(name))
    #   Expect a ValueError to happen and handle it appropriately...remember to test it out!
    try:
        num_tickets = int(num_tickets)
        #   Raise a ValueError if the request is for more tickets than are available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        #   Include the error text in the output
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        #   Calculate the price (number of tickets multiplied by the price) and assign it to a variable
        amount_due = calculate_price(num_tickets)
        #   Output the price to the screen
        print("The total due is ${}".format(amount_due))
        #   Prompt user if they want to proceed.    Y/N?
        should_proceed = input("Do you want to proceed? Y/N ")
        #   If they want to proceed
        if should_proceed.lower() == 'y':
            #   Print out to the screen "SOLD!" to confirm purchase
            #   TODO:   Gather credit card information and process it.
            print("SOLD!")
            #   and the decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= num_tickets
        #   Otherwise.....
        else:
            #   Thank them by name
            print("Thank you anyways, {}!".format(name))

#   Notify user that the tickets are sold out
print("Sorry the tickets are all sold out!!!")
