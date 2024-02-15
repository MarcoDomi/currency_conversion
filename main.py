import currencyapicom
import sys


def print_values(base_pair, converted_values):
    print(f"\nBASE CURRENCY\n{base_pair[0]}: {base_pair[1]}")
    print("-" * 5)

    for code in converted_values:
        print(f"{code}: {converted_values[code]}")


def convert(base_value, exchange_rate):
    return base_value * exchange_rate


client = currencyapicom.Client("cur_live_5X7DY8sMMB7D1OCA741glYl7mrdiCy9sPz1VDics")

base_curr = sys.argv[1]
other_curr = sys.argv[2:]
base_value = float(input(f"Enter a {base_curr} amount: "))

result = client.latest(base_curr, other_curr)
other_curr = result["data"]

converted_values = {}
for key in other_curr:
    other_val = other_curr[key]["value"]
    converted_values[key] = convert(base_value, other_val)

base_pair = (base_curr, base_value)
print_values(base_pair, converted_values)