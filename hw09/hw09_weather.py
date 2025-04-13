def read_db(filename):
    total_temp = 0
    temp_count = 0
    total_rain = 0
    rain_days_over_5mm = 0

    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            if len(tokens) < 10:
                continue

            tavg_str = tokens[4]
            rainfall_str = tokens[9]

            if tavg_str:
                try:
                    tavg = float(tavg_str)
                    total_temp += tavg
                    temp_count += 1
                except ValueError:
                    pass

            if rainfall_str:
                try:
                    rainfall = float(rainfall_str)
                    total_rain += rainfall

                    if rainfall >= 5:
                        rain_days_over_5mm += 1
                except ValueError:
                    pass

    avg_temp = total_temp / temp_count if temp_count > 0 else 0
    return avg_temp, rain_days_over_5mm, total_rain


def main():
    filename = "./weather(146)_2022-2022.csv"
    avg_temp, rain_over_5mm_days, total_rain = read_db(filename)

    print(f"연 평균 기온: {avg_temp:.2f}°C")
    print(f"5mm 이상 강우일수: {rain_over_5mm_days}일")
    print(f"총 강우량: {total_rain:.1f}mm")


if __name__ == "__main__":
    main()
