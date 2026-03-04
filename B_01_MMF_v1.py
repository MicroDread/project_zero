# functions
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_checker(questions, valid_answers=('yes', 'no'),
                   num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(questions).lower()

        for item in valid_answers:

            # check if response is the entire word
            if response == item:
                return item

            # check if the response is the entire word
            if response == item:
                return item

            # check if its == item[0]
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


def instructions():
    make_statement( "instructions", "")

    print("""
    
For each ticket holder enter ...
- Their name 
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the
exit code ('xxx'), the program will display the ticket 
 sales information and write the data to a text file.
 
 it will also choose one lucky ticket holder who wins the 
 draw (their ticket is free)


""")


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank.  Please try again.\n")


def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # return response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)



# Main routine goes here

# Initialise ticket number
MAX_TICKETS = 7
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement( "Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_checker("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    # ask user for their name (and check it's not blank
    print()
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

        # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_checker("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets. ")