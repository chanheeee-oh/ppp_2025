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

    total_rainfall = sum(rainfalls)


    with open("강우량_결과.txt", "w", encoding="utf-8") as f:
        f.write(f"{year}년 총 강우량은 {total_rainfall:.1f}mm입니다\n")

if __name__ == "__main__":
    main()

