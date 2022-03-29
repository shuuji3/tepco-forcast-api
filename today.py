import io

import dateutil.parser
import pandas as pd
import requests

TEPCO_CSV_URL = 'https://www.tepco.co.jp/forecast/html/images/juyo-d-j.csv'


def get_tepco_csv_text():
    r = requests.get(TEPCO_CSV_URL)
    r.encoding = 'shift-jis'
    return r.text


def extract_csv(skiprows: int = None, nrows: int = None) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(TEPCO_CSV_TEXT), encoding='shift-jis', skiprows=skiprows, nrows=nrows)


def get_update_time():
    update_time_string = extract_csv(nrows=0).columns[0][:15]
    return dateutil.parser.parse(update_time_string)


def get_peak_period_supply():
    return extract_csv(skiprows=1, nrows=1)


def get_expected_maximum_power():
    return extract_csv(skiprows=3, nrows=1)


def get_usage_peak_period_supply():
    return extract_csv(skiprows=6, nrows=1)


def get_usage_peak_period_expected_power():
    return extract_csv(skiprows=9, nrows=1)


def get_daily_results_hourly():
    return extract_csv(skiprows=12, nrows=24)


def get_maximum_usage():
    return extract_csv(skiprows=38, nrows=1)


def get_peak_period_suppy_tomorrow():
    return extract_csv(skiprows=42, nrows=1)


def get_expected_maximum_power_tomorrow():
    return extract_csv(skiprows=44, nrows=1)


def get_usage_peak_period_supply_tomorrow():
    return extract_csv(skiprows=48, nrows=1)


def get_usage_peak_period_expected_power_tomorrow():
    return extract_csv(skiprows=50, nrows=1)


def get_today_results_per_5min():
    return extract_csv(skiprows=54)


TEPCO_CSV_TEXT = get_tepco_csv_text()


if __name__ == '__main__':

    data_type_pairs = [
        ('peak_period_supply', get_peak_period_supply),
        ('expected_maximum_power', get_expected_maximum_power),
        ('usage_peak_period_supply', get_usage_peak_period_supply),
        ('usage_peak_period_expected_power', get_usage_peak_period_expected_power),
        ('daily_results_hourly', get_daily_results_hourly),
        ('maximum_usage', get_maximum_usage),
        ('peak_period_suppy_tomorrow', get_peak_period_suppy_tomorrow),
        ('expected_maximum_power_tomorrow', get_expected_maximum_power_tomorrow),
        ('usage_peak_period_supply_tomorrow', get_usage_peak_period_supply_tomorrow),
        ('usage_peak_period_expected_power_tomorrow', get_usage_peak_period_expected_power_tomorrow),
        ('today_results_per_5min', get_today_results_per_5min),
    ]

    for data_type, get_data in data_type_pairs:
        data = get_data()
        data.to_json(f'public/api/{data_type}.json', indent=2, force_ascii=False)
