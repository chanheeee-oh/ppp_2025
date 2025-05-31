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

def get_rainfall_sum(filename):
    df = pd.read_csv(filename, skipinitialspace=True)

    if "rainfall" in df.columns:
        return df["rainfall"].dropna().sum()
    else:
        return None

def main():
    station_id = 146
    year = 2012
    filename = f"./weather_{station_id}_{year}.csv"

    download_weather_data(station_id, year, filename)

    total_rainfall = get_rainfall_sum(filename)

    if total_rainfall is not None:
        print(f"{year}년 총 강수량은 {total_rainfall:.1f}mm입니다")
    else:
        print(f"{year}년의 강수량 데이터가 부족하여 계산할 수 없습니다.")

if __name__ == "__main__":
    main()

