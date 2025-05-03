import os
import requests

def download_weather_data(station_id, year, filename):
    if os.path.exists(filename):
        pass
    else:
        url = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8-sig") as f:
            f.write(resp.text)

def get_weather_data_float(filename, col_idx):
    weather_data = []

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            columns = line.strip().split(",")
            if col_idx < len(columns):
                value = columns[col_idx].strip()
                if value:
                    weather_data.append(float(value))

    return weather_data

def main():
    station_id = 146
    year = 2022
    filename = f"./weather_{station_id}_{year}.csv"

    download_weather_data(station_id, year, filename)

    rain_col_idx = 9
    rainfalls = get_weather_data_float(filename, rain_col_idx)

    days_over_5mm = 0
    for rain in rainfalls:
        if rain >= 5.0:
            days_over_5mm += 1


    with open("5mm_이상_강우일수.txt", "w", encoding="utf-8") as f:
        f.write(f"{year}년 동안 5mm 이상 강우일수는 {days_over_5mm}일입니다\n")

if __name__ == "__main__":
    main()


