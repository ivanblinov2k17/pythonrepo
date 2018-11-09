from trades.trades_logic import initArr, \
    dividing_window_by_markets, \
    longest_window, \
    longest_windows_by_markets

transactions, market_list = initArr('test_trade.csv')

main_window_start, main_window_len, main_window_sum, main_window_start_time\
    = longest_window(transactions)

division = dividing_window_by_markets(transactions, market_list,
                                      main_window_start, main_window_len)

windows_by_markets = longest_windows_by_markets(transactions, market_list)

print("Main window")
print(main_window_start_time, main_window_len, main_window_sum)
print("Dividing main window by markets")
for div in division:
    print(div)
print("Dividing transactions by markets and finding longest window there")
for window in windows_by_markets:
    print(window)

