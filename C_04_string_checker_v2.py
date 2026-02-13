# functions go here
from http.client import responses
from statistics import median_low

from Tools.scripts.stable_abi import itemclass


def string_checker(questions, valid_ans_list, num_letters):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(questions).lower()

        for item in valid_ans_list:

            # check if response is the entire word
            if responses == item:
                return item

            # check if the response is the entire word
            if response == item:
                return item

            # check if its == item[0]
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")


# main routine goes here
yes_no_list = ['yes','no']
payment_list = ['cash', 'credit']

like_coffee = string_checker( "Do you like coffee? ",
                            yes_no_list, 1)
print(f"You chose {like_coffee}")
pay_method = string_checker( "payment method: ", payment_list, 2)
print(f"you chose{pay_method}")