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

def get_max_tmax(filename):

    df = pd.read_csv(filename, skipinitialspace=True)

    if "tmax" in df.columns:
        return df["tmax"].dropna().max()
    else:
        return None

def main():
    station_id = 146
    year = 2024
    filename = f"./weather_{station_id}_{year}.csv"

    download_weather_data(station_id, year, filename)

    max_temp = get_max_tmax(filename)

    if max_temp is not None:
        print(f"{year}년 최고 기온은 {max_temp:.1f}도입니다.")
    else:
        print(f"{year}년의 최고 기온 데이터가 부족하여 계산할 수 없습니다.")

if __name__ == "__main__":
    main()
