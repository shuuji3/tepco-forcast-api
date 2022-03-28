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


def get_update_time():
    update_time_string = extract_csv(nrows=0).columns[0][:15]
    return dateutil.parser.parse(update_time_string)
