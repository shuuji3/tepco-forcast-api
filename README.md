# tepco-forecast-api
💡 Experiment to convert the TEPCO's irregular CSV files to the machine readable JSON files

## Example

```py
> ipython

In [1]: df=pd.read_json('http://shuuji3.xyz/tepco-forecast-api/api/today_results_per_5min.json')

In [2]: df[df['当日実績(５分間隔値)(万kW)'].isna() == False]
Out[2]:
          DATE   TIME  当日実績(５分間隔値)(万kW)  太陽光発電実績(５分間隔値)(万kW)
0   2022-06-27   0:00            2846.0                  0.0
1   2022-06-27   0:05            2836.0                  0.0
2   2022-06-27   0:10            2803.0                  0.0
3   2022-06-27   0:15            2784.0                  0.0
4   2022-06-27   0:20            2770.0                  0.0
..         ...    ...               ...                  ...
208 2022-06-27  17:20            4777.0                148.0
209 2022-06-27  17:25            4756.0                127.0
210 2022-06-27  17:30            4729.0                111.0
211 2022-06-27  17:35            4707.0                 98.0
212 2022-06-27  17:40            4698.0                 87.0

[213 rows x 4 columns]
```
