import currencyapicom
import sys

'''
POSSIBLE INCORRECT INPUTS
12
12.3
12.34345464876
'''
def append_zero(digit_str:str) -> str:
    '''append a zero to digit string if needed'''
    digit_list = digit_str.split('.')
    digits_after_decimal = digit_list[1]

    if len(digits_after_decimal) == 1:
        digit_str += '0'
    
    return digit_str


# there is no reason to check if number of digits after decimal is 1 for input b/c it will be converted to a float afterwards which will remove appended 0
def format_input(digit_str: str) -> float:
    '''ensure currency amount inputted is correctly formatted'''
    if digit_str.find(".") == -1:#if no decimal point found in input 
        correct_currency_amount = digit_str + ".0" #append .0  to string
    else: 
        #if no decimal was found there is no reason to execute commands under else statement
        #split digit string by decimal and store the digits after the decimal
        digit_list = digit_str.split(".") 
        digits_after_decimal = digit_list[1]

        #if digits count after decimal is greater than 2 use slicing to remove extra digits and store in digit list
        if len(digits_after_decimal) > 2:
            digit_list[1] = digits_after_decimal[:2]

        correct_currency_amount = ".".join(digit_list) #rejoin digit list using a decimal point

    return float(correct_currency_amount) #convert to float and return


def print_values(base_currency_code, base_currency_amount, converted_values):
    '''print all info related to currency conversion'''
    print(f"\nBASE CURRENCY\n{base_currency_code}: {base_currency_amount}") 
    print("-" * 5)
    for code, value in converted_values.items():
        print(f"{code}: {value}")


def convert(base_value:float, exchange_rate:float):
    '''perform currency conversion by multiplying base value with exchange rate'''
    return base_value * exchange_rate 


def get_converted_values(base_amount, currency_data):
    '''get dictionary of converted base values for each desired currency'''
    converted_values = {}
    for key in currency_data:  #iterate thru other currencies
        other_value = currency_data[key]["value"]  #obtain exchange rate relative to base currency for current 'other currency'
        converted_values[key] = convert(base_amount, other_value)  #perform conversion

    return converted_values


client = currencyapicom.Client("cur_live_5X7DY8sMMB7D1OCA741glYl7mrdiCy9sPz1VDics")

base_currency_code = sys.argv[1]   #first command line arg is the base currency
other_currency_code = sys.argv[2:] #all following command line args are currencies the base currency will be converted to
base_value = format_input(input(f"Enter a {base_currency_code} amount: ")) #enter currency amount and ensure the amount is formatted correctly

result = client.latest(base_currency_code, other_currency_code)#use api to obtain latest currency exchange rates of 'other currency' relative to base currency
other_currency_data = result["data"]  #store data about the other currency codes

converted_values = get_converted_values(base_value, other_currency_data)

# it is guaranteed the num of digits after decimal will not exceed 2 by this point
base_value = append_zero(str(base_value)) 
print_values(base_currency_code, base_value, converted_values)
