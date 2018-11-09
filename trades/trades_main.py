from trades.trades_logic import initArr
transactions, market_list = initArr('test_trade.csv')
for t in transactions:
    print(t)

