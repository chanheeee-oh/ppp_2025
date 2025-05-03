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
        lines = f.readlines()[1:]  # 헤더 제외
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

    temp_col_idx = 3
    temps = get_weather_data_float(filename, temp_col_idx)

    if temps:
        avg_temp = sum(temps) / len(temps)
        result = f"{year}년 연 평균 기온은 {avg_temp:.2f}℃입니다\n"
    else:
        result = f"{year}년 기온 데이터가 없습니다\n"

    with open("기온_결과.txt", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    main()

