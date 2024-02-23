import currencyapicom
import sys

'''
POSSIBLE INCORRECT INPUTS
12
12.3
12.34345464876
'''
def check_digit_length(digits_str):
    digit_count = len(digits_str)

    if digit_count == 1:
        digits_str += "0"
    elif digit_count > 2:
        digits_str = digits_str[:2] 

    return digits_str

def fix_input(num: float) -> str:
    s = str(num)

    digit_list = s.split(".")
    digits_after_decimal = digit_list[1]

    digit_list[1] = check_digit_length(digits_after_decimal)

    correct_currency_amount = ".".join(digit_list)
    return correct_currency_amount


def print_values(base_currency_code, base_currency_amount, converted_values):

    print(f"\nBASE CURRENCY\n{base_currency_code}: {base_currency_amount}") 
    print("-" * 5)
    for code, value in converted_values.items():
        print(f"{code}: {value}")


def convert(base_value, exchange_rate):
    return float(base_value) * exchange_rate


client = currencyapicom.Client("cur_live_5X7DY8sMMB7D1OCA741glYl7mrdiCy9sPz1VDics")

base_currency_code = sys.argv[1]
other_currency_code = sys.argv[2:]
base_value = fix_input(float(input(f"Enter a {base_currency_code} amount: ")))

result = client.latest(base_currency_code, other_currency_code)
other_currency_data = result["data"]

converted_values = {}
for key in other_currency_data:
    other_value = other_currency_data[key]["value"]
    converted_values[key] = convert(base_value, other_value)


print_values(base_currency_code, base_value, converted_values)
