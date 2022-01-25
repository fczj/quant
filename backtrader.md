# ÖØ²ÉÑù
```
    data = bt.feeds.GenericCSVData(
        dataname="2022_01.csv",
        fromdate=datetime.datetime(2022, 1, 15),
        todate=datetime.datetime(2022, 1, 21),
        dtformat='%Y-%m-%d %H:%M:%S',
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        openinterest=-1,
        timeframe=bt.TimeFrame.Minutes,
    )

    cerebro.resampledata(data, timeframe=bt.TimeFrame.Minutes, compression=60*24, name="BTC_HOUR")
```
