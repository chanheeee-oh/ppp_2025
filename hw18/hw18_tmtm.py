import os
import requests
import pandas as pd

def download_weather_data(station_id, year, filename):
    if not os.path.exists(filename):
        url = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8-sig") as f:
            f.write(resp.text)

def get_max_diurnal_range(filename):
    df = pd.read_csv(filename, skipinitialspace=True)

    if "tmax" in df.columns and "tmin" in df.columns:
        valid = df[["tmax", "tmin"]].dropna()
        diff = valid["tmax"] - valid["tmin"]
        return diff.max()
    else:
        return None

def main():
    station_id = 146
    year = 2020
    filename = f"./weather_{station_id}_{year}.csv"

    download_weather_data(station_id, year, filename)

    max_range = get_max_diurnal_range(filename)

    if max_range is not None:
        print(f"{year}년 최대 일교차는 {max_range:.1f}도입니다.")
    else:
        print(f"{year}년의 tmax 또는 tmin 데이터가 부족하여 계산할 수 없습니다.")

if __name__ == "__main__":
    main()
