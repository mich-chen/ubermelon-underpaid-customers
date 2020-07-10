""" Checks if customers underpaid for melons """
# great example file to practice Classes

# need to also write a function to idenitfy any new customers
# need to write function to calculate expected cost
# only Sean and Ashley are the only customers who didn't pay correctly

melon_cost = 1.00

def lines_into_list(line):
    """ takes file with lines and strips, and splits to return a list of item words """

    words = line.rstrip().split('|')
    return words


def calculate_expected_cost(melon_cost, melon_count):
    """ calculates expected cost based on number of melons customer bought"""

    return melon_cost + melon_count


def convert_to_floats(str_lst):
    """ takes list of strings and converts them into floats """

    float_order = []
    for string in str_lst:
        float_order.append(float(string))

    return float_order


def check_order(customer_name, expected_cost, customer_paid):
    """ check if customer paid expected amount and prints statement if no """

    if expected_cost != customer_paid:
        if expected_cost > customer_paid:
            payment_status = "UNDERPAID"
        else: 
            payment_status = "OVERPAID"

        print(f"    {customer_name} {payment_status} for their melons!")

    else:
        pass


def payment_info_and_status(report):
    """ opens a text file, converts each line into a list of strings of each element in line"""

    order_data = open(report)
    for line in order_data:
        order = lines_into_list(line) # function will split each line by '|' and get a list of strings
        # each order has 4 strings
        order[0:1] = []
        name = order.pop(0)
        order_as_floats = convert_to_floats(order)
        melon_count, paid = order_as_floats
        expected_cost = calculate_expected_cost(melon_cost, melon_count)
        print(f"{name} paid ${paid:.2f}, expected ${expected_cost:.2f}")
        check_order(name, expected_cost, paid)
    order_data.close()


payment_info_and_status("customer-orders.txt")
