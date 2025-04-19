def get_weather_data_by_year(filename):
    rain_2021 = 0
    rain_2022 = 0

    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")

            if tokens[0] != "" and tokens[9] != "":
                year = int(tokens[0])
                rain = float(tokens[9])

                if rain > 0:
                    if year == 2021:
                        rain_2021 += rain
                    elif year == 2022:
                        rain_2022 += rain

    return rain_2021, rain_2022


def main():
    filename = "./weather(146)_2001-2022.csv"
    rain_2021, rain_2022 = get_weather_data_by_year(filename)

    print(f"2021년 총 강수량은 {rain_2021:.1f}mm입니다")
    print(f"2022년 총 강수량은 {rain_2022:.1f}mm입니다")


if __name__ == "__main__":
    main()
