import requests
import json


def get_conversions(currency_code, codes_to_get=None):
    if codes_to_get is None:
        codes_to_get = {'usd', 'eur'}
    result = {}
    CURRENCY_RESOURCE = 'http://www.floatrates.com/daily/'
    response = requests.get(f'{CURRENCY_RESOURCE}{currency_code}.json')
    if response:
        currency_json = json.loads(response.content)
        for item in currency_json:
            if item in codes_to_get:
                result[item] = currency_json[item]
    return result


def print_converted_amount(currency_amount, currency_code_to, currency_json):
    conversion_code = currency_json[currency_code_to]
    converted_amount = round(currency_amount * conversion_code['rate'], 2)
    print(f'You received {converted_amount} {currency_code_to.upper()}.')


def currency_converter():
    currency_code_from = input()
    currency_json = get_conversions(currency_code_from.lower())

    while True:
        currency_code_to = input()
        if currency_code_to == "":
            break
        currency_amount = float(input())

        print('Checking the cache...')
        if currency_code_to.lower() in currency_json:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            currency_json[currency_code_to.lower()] = \
                get_conversions(currency_code_from.lower(), {currency_code_to.lower()})[currency_code_to.lower()]

        print_converted_amount(currency_amount, currency_code_to.lower(), currency_json)


if __name__ == '__main__':
    currency_converter()
