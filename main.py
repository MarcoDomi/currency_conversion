import currencyapicom
import sys

'''
POSSIBLE INCORRECT INPUTS
12
12.3
12.34345464876
'''
def fix_input(num: float) -> str:
    s = str(num)
    
    digit_list = s.split(".")
    digits_after_decimal = digit_list[1]

    if len(digits_after_decimal) == 1:
        digit_list[1] += "0"
    elif len(digits_after_decimal) > 2:
        digit_list[1] = digits_after_decimal[:2]

    return ".".join(digit_list)


def print_values(base_currency_pair, converted_values):
    base_currency_code = base_currency_pair[0] #base currency code
    base_currency_amount = fix_input(base_currency_pair[1]) #base currency amount

    print(f"\nBASE CURRENCY\n{base_currency_code}: {base_currency_amount}\n") #why not return error?
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
    other_val = other_currency_data[key]["value"]
    converted_values[key] = convert(base_value, other_val)

base_pair = (base_currency_code, base_value)
print_values(base_pair, converted_values)
