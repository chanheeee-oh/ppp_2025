def get_weather_data(filename, col_idx):
    weather_datas = []

    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[col_idx] != "":
                weather_datas.append(float(tokens[col_idx]))

    return weather_datas


def get_sunshine_events(filename):
    top3_tmax = sorted(get_weather_data(filename, 3), reverse=True)[:3]
    print(f"가장 높았던 최고기온 3개는 {top3_tmax}입니다")


def main():
    filename = "./weather(146)_2022-2022.csv"
    get_sunshine_events(filename)


if __name__ == "__main__":
    main()

