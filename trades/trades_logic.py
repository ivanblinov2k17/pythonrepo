import csv
from datetime import datetime


def initArr(name):
    transactions = []
    market_list = set()
    trades_file = open(name, 'r')
    reader = csv.reader(trades_file)
    for trades_row in reader:
        time, price, size, exchange = trades_row
        if trades_row != ['Time', 'Proce', 'Size', 'Exchange']:
            time = datetime.strptime(time, '%H:%M:%S.%f')
            price = float(price)
            size = int(size)
            transactions.append([time, price, size, exchange])
            market_list.add(exchange)
    return transactions, market_list


def longest_window(transactions):
    second = datetime.strptime('1', '%S')
    zero = datetime.strptime('0', '%S')
    i = 0
    k = []
    t = i
    while i < len(transactions):
        while i < len(transactions) \
                and transactions[i][0] - transactions[t][0] < second - zero:
            i += 1
        k.append([t, i-1])
        t = i
    window_len = 0
    window_start = 0
    sum_transactions = 0
    for i in range(len(k)):
        if k[i][1]-k[i][0] > window_len:
            window_len = k[i][1]-k[i][0]
            window_start = i
    for i in range(window_start, window_start + window_len):
        sum_transactions += transactions[i][1]*transactions[i][2]
    return window_start, window_len, sum_transactions


def dividing_transactions_by_market(transactions, market):
    transactions_by_market = []

    for transaction in transactions:
        if transaction[3] == market:
            transactions_by_market.append(transaction)

    return transactions_by_market


def longest_window_by_market(transactions, market):
    transactions_by_market = dividing_transactions_by_market(transactions, market)
    return longest_window(transactions_by_market)


def dividing_window_by_markets(transactions, market_list, window_start, window_len):
    division = []
    for market in market_list:
        sum_transactions = 0
        num_transactions = 0
        start_transaction = 0
        for i in range(window_start, window_start+window_len):
            if transactions[i][3] == market:
                if num_transactions == 0:
                    start_transaction = i
                num_transactions += 1
                sum_transactions += transactions[i][1] * transactions[i][2]
        division.append([market, start_transaction, num_transactions, sum_transactions])
    return division


def longest_windows_by_markets(transactions, market_list):
    windows = []
    for market in market_list:
        window = longest_window_by_market(transactions, market)
        windows.append([market, window])
    return windows
