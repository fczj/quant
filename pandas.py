from datetime import datetime
import pickle
from pprint import pprint
import pandas as pd

def timstamp_to_date(timestamp):
    from datetime import datetime
    dt_obj = datetime.fromtimestamp(timestamp / 1000)
    return dt_obj


# 数据聚合
with open("2019-10-01", "rb") as f:
    data = pickle.load(f)

    df = pd.DataFrame(data, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    # df['datetime'] = df['datetime'].map(lambda x: int(x / 1000))
    # df['datetime'] = pd.to_datetime(df['datetime'], unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')

    # df.columns = df.columns.get_level_values(0)
    df = df.set_index('datetime')
    # df.index = pd.to_datetime(df.index, errors='coerce')
    # df.index = pd.to_datetime(df.index, errors='coerce')
    #
    b = df.resample('1d').agg({'open': 'first',
                               'high': 'max',
                               'low': 'min',
                               'close': 'last',
                               'volume': 'sum'
                               })
    print(b)
