import mexc_spot_v3


market = mexc_spot_v3.mexc_market()

# Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
# If there are no parameters, no need to send params
params = {
    "symbol": "BTCUSDT",
    "interval": "30m",
    "limit": "100",
    # "startTime": "1705029500000",
    # "endTime": "1705029599909"
}
Kline = market.get_kline(params)
close=[k[4] for k in Kline]
print(close)