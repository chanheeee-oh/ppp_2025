def get_weather_data(filename, col_idx):
    weather_datas = []

    with open (filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")

            weather_datas.append(float(tokens[col_idx]))

    return weather_datas


def sumifs(rainfalls, months, selected=[6, 7, 8]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected and rain > 0:
            total += rain
    return total

def main():
    filename = "./weather(146)_2022-2022.csv"
    rainfalls = get_weather_data(filename, 9)
    months = get_weather_data(filename, 1)

    summer_rain = sumifs(rainfalls, months, selected=[6, 7, 8])
    print(f"여름철 강수량은 {summer_rain:.1f}mm입니다")

if __name__ == "__main__":
    main()