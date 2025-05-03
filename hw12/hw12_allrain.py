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
    filename = "./weather(146)_2020-2020.csv"


    rain_col_idx = 9
    rainfalls = get_weather_data_float(filename, rain_col_idx)

    total_rainfall = sum(rainfalls)

    print(f"총 강우량은 {total_rainfall:.1f}mm입니다")


if __name__ == "__main__":
    main()
