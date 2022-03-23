import io

import dateutil.parser
import pandas as pd
import requests

TEPCO_CSV_URL = 'https://www.tepco.co.jp/forecast/html/images/juyo-d-j.csv'


def get_tepco_csv_text():
    r = requests.get(TEPCO_CSV_URL)
    r.encoding = 'shift-jis'
    return r.text


TEPCO_CSV_TEXT = get_tepco_csv_text()


def extract_csv(skiprows: int = None, nrows: int = None) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(TEPCO_CSV_TEXT), encoding='shift-jis', skiprows=skiprows, nrows=nrows)


def pretty(df: pd.DataFrame) -> None:
    print(df.to_json(force_ascii=False, indent=2))


def pretty_one(df: pd.DataFrame) -> None:
    print(df.iloc[0].to_json(force_ascii=False, indent=2))


def get_update_time():
    update_time_string = extract_csv(nrows=0).columns[0][:15]
    return dateutil.parser.parse(update_time_string)


print(get_update_time())
# Out[108]: '2022-03-22 12:45:00'

pretty_one(extract_csv(skiprows=1, nrows=1))
# Out[13]:
#    ピーク時供給力(万kW)          時間帯 供給力情報更新日 供給力情報更新時刻  ピーク時予備率(%)  ピーク時使用率(%)
# 0          4753  16:00〜17:00     3/22     12:00           0         100

pretty_one(extract_csv(skiprows=3, nrows=1))
# Out[14]:
#    予想最大電力(万kW)          時間帯 予想最大電力情報更新日 予想最大電力情報更新時刻
# 0         4753  16:00〜17:00        3/22        12:00

pretty_one(extract_csv(skiprows=6, nrows=1))
# Out[17]:
#    使用率ピーク時供給力(万kW)          時間帯 供給力情報更新日 供給力情報更新時刻  使用率ピーク時予備率(%)  使用率ピーク時使用率(%)
# 0             4753  16:00〜17:00     3/22     12:00              0            100

pretty_one(extract_csv(skiprows=9, nrows=1))
# Out[20]:
#    使用率ピーク時予想電力(万kW)          時間帯 予想電力情報更新日 予想電力情報更新時刻
# 0              4753  16:00〜17:00      3/22      12:00

pretty(extract_csv(skiprows=12, nrows=24))
# Out[26]:
#          DATE   TIME  当日実績(万kW)  予測値(万kW)  使用率(%)  供給力想定値(万kW)
# 0   2022/3/22   0:00       2592         0    80.0         3214
# 1   2022/3/22   1:00       2507         0    78.0         3178
# 2   2022/3/22   2:00       2507         0    79.0         3141
# 3   2022/3/22   3:00       2540         0    81.0         3107
# 4   2022/3/22   4:00       2607         0    84.0         3095
# 5   2022/3/22   5:00       2766         0    88.0         3136
# 6   2022/3/22   6:00       3092         0    82.0         3737
# 7   2022/3/22   7:00       3496         0    86.0         4065
# 8   2022/3/22   8:00       3983         0    95.0         4190
# 9   2022/3/22   9:00       4349         0    97.0         4461
# 10  2022/3/22  10:00       4455         0   101.0         4393
# 11  2022/3/22  11:00       4515         0   103.0         4355
# 12  2022/3/22  12:00          0      4483     NaN         4334
# 13  2022/3/22  13:00          0      4625     NaN         4351
# 14  2022/3/22  14:00          0      4726     NaN         4345
# 15  2022/3/22  15:00          0      4744     NaN         4337
# 16  2022/3/22  16:00          0      4843     NaN         4293
# 17  2022/3/22  17:00          0      4803     NaN         4231
# 18  2022/3/22  18:00          0      4715     NaN         4187
# 19  2022/3/22  19:00          0      4548     NaN         4256
# 20  2022/3/22  20:00          0      4354     NaN         4273
# 21  2022/3/22  21:00          0         0     NaN         3997
# 22  2022/3/22  22:00          0         0     NaN         3732
# 23  2022/3/22  23:00          0         0     NaN         3441

pretty_one(extract_csv(skiprows=38, nrows=1))
# Out[52]:
# 最大使用率(%)          時間帯
# 0       103  11:00〜12:00

pretty_one(extract_csv(skiprows=42, nrows=1))
# Out[60]:
# 翌日のピーク時供給力(万kW)  時間帯  供給力情報更新日  供給力情報更新時刻  ピーク時予備率(%)  ピーク時使用率(%)
# 0              NaN  NaN       NaN        NaN         NaN         NaN

pretty_one(extract_csv(skiprows=44, nrows=1))
# Out[61]:
# 翌日の予想最大電力(万kW)  時間帯  予想最大電力情報更新日  予想最大電力情報更新時刻
# 0             NaN  NaN          NaN           NaN

pretty_one(extract_csv(skiprows=48, nrows=1))
# Out[83]:
# 翌日の使用率ピーク時供給力(万kW)  時間帯  供給力情報更新日  供給力情報更新時刻  使用率ピーク時予備率(%)  使用率ピーク時使用率(%)
# 0                 NaN  NaN       NaN        NaN            NaN            NaN

pretty_one(extract_csv(skiprows=50, nrows=1))
# Out[84]:
# 翌日の使用率ピーク時予想電力(万kW)  時間帯  予想電力情報更新日  予想電力情報更新時刻
# 0                  NaN  NaN        NaN         NaN

pretty(extract_csv(skiprows=54))
# Out[87]:
# DATE   TIME  当日実績(５分間隔値)(万kW)  太陽光発電実績(５分間隔値)(万kW)
# 0    2022/3/22   0:00            2687.0                  0.0
# 1    2022/3/22   0:05            2647.0                  0.0
# 2    2022/3/22   0:10            2643.0                  0.0
# 3    2022/3/22   0:15            2635.0                  0.0
# 4    2022/3/22   0:20            2622.0                  0.0
# ..         ...    ...               ...                  ...
# 283  2022/3/22  23:35               NaN                  NaN
# 284  2022/3/22  23:40               NaN                  NaN
# 285  2022/3/22  23:45               NaN                  NaN
# 286  2022/3/22  23:50               NaN                  NaN
# 287  2022/3/22  23:55               NaN                  NaN
#
# [288 rows x 4 columns]
