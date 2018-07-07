#获取个股历史交易数据（包括均线数据）：
import pandas as pd
import tushare as ts
d=ts.get_hist_data('601318',start='2018-01-01',end='2018-07-07') #一次性获取全部数据