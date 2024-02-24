import currencyapicom
import sys

'''
POSSIBLE INCORRECT INPUTS
12
12.3
12.34345464876
'''

def check_digit_length(digit_str:str) -> str:
    digit_list = digit_str.split('.')
    digits_after_decimal = digit_list[1]

    if len(digits_after_decimal) == 1:
        digit_str += '0'
    
    return digit_str


def format_input(digit_str: str) -> float:

    if digit_str.find(".") == -1:
        correct_currency_amount = digit_str + ".0"
    else:
        digit_list = digit_str.split(".")
        digits_after_decimal = digit_list[1]

        if len(digits_after_decimal) > 2:
            digit_list[1] = digits_after_decimal[:2]

        correct_currency_amount = ".".join(digit_list)
        
    return float(correct_currency_amount)


def print_values(base_currency_code, base_currency_amount, converted_values):
    
    print(f"\nBASE CURRENCY\n{base_currency_code}: {base_currency_amount}") 
    print("-" * 5)
    for code, value in converted_values.items():
        print(f"{code}: {value}")


def convert(base_value:float, exchange_rate:float):
    return base_value * exchange_rate


client = currencyapicom.Client("cur_live_5X7DY8sMMB7D1OCA741glYl7mrdiCy9sPz1VDics")

base_currency_code = sys.argv[1]
other_currency_code = sys.argv[2:]
base_value = format_input(input(f"Enter a {base_currency_code} amount: "))

result = client.latest(base_currency_code, other_currency_code)
other_currency_data = result["data"]

converted_values = {}
for key in other_currency_data:
    other_value = other_currency_data[key]["value"]
    converted_values[key] = convert(base_value, other_value)

base_value = check_digit_length(str(base_value))
print_values(base_currency_code, base_value, converted_values)
