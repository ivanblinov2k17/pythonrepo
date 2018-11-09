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
            time = datetime.strptime(time, '%H:%M:%S.%f').time()
            price = float(price)
            size = int(size)
            transactions.append([time, price, size, exchange])
            market_list.add(exchange)
    return transactions, market_list


second = datetime.strptime('1','%S').time()
zero = datetime.strptime('0', '%S').time()

