def get_weather_data_float(filename, col_idx):
    weather_datas = []

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[col_idx] != "":
                weather_datas.append(float(tokens[col_idx]))

    return weather_datas


def main():
    filename = "./weather(146)_2020-2020.csv"


    temp_col_idx = 3
    daily_avg_temps = get_weather_data_float(filename, temp_col_idx)

    if daily_avg_temps:
        annual_avg_temp = sum(daily_avg_temps) / len(daily_avg_temps)
        print(f"연 평균 기온은 {annual_avg_temp:.2f}℃입니다")
    else:
        print("기온 데이터가 없습니다.")


if __name__ == "__main__":
    main()
