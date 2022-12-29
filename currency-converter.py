def get_global_currencies(coins):
    currency_conversions = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
    for currency in currency_conversions:
        amount = round(currency_conversions[currency] * coins, 2)
        print(f'I will get {amount} {currency} from the sale of {coins} conicoins.')


def convert_coni_coins(coins, exchange_rate):
    return coins * exchange_rate


def currency_converter():
    coni_coin_count = float(input())
    get_global_currencies(coni_coin_count)


if __name__ == '__main__':
    currency_converter()
