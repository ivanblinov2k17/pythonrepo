import csv
from datetime import datetime


def initArr(name):
    transactions = []
    market_list = set()
    trades_file = open(name, 'r')
    reader = csv.reader(trades_file)
    for trades_row in reader:
        if trades_row != '' and trades_row != ' ' and \
                trades_row != '\n':
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
    j = 0
    while i < len(transactions):
        while j < len(transactions) and \
                (transactions[j][0]-transactions[i][0] < second-zero):
            j += 1
        k.append([i, j-1])
        i += 1
        j = i
    max_start = 0
    max_len = 0
    for elem in k:
        if elem[1]-elem[0] + 1 > max_len:
            max_len = elem[1] - elem[0] + 1
            max_start = elem[0]
    max_sum = 0
    for i in range(max_start, max_start+max_len):
        max_sum += transactions[i][1]*transactions[i][2]
    window_start_time = 0
    if len(transactions) > 0:
        window_start_time = str(transactions[max_start][0].time())
    return max_start, max_len, max_sum, window_start_time

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
        trans_time = str(transactions[start_transaction][0].time())
        division.append([market, trans_time, num_transactions, sum_transactions])
    return division


def dividing_transactions_by_market(transactions, market):
    transactions_by_market = []

    for transaction in transactions:
        if transaction[3] == market:
            transactions_by_market.append(transaction)

    return transactions_by_market


def longest_window_by_market(transactions, market):
    transactions_by_market = dividing_transactions_by_market(transactions, market)
    return longest_window(transactions_by_market)


def longest_windows_by_markets(transactions, market_list):
    windows = []
    for market in market_list:
        window = longest_window_by_market(transactions, market)
        windows.append([market, window[3], window[1], window[2]])
    return windows