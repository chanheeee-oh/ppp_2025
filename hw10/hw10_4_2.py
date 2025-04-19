def get_weather_data_int(filename, col_idx):
    weather_datas = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[col_idx] != "":
                weather_datas.append(int(float(tokens[col_idx])))

    return weather_datas

def get_rain_event_amounts(rainfalls):
    events = []
    current_event_total = 0
    for rain in rainfalls:
        if rain > 0:
            current_event_total += rain
        else:
            if current_event_total > 0:
                events.append(current_event_total)
                current_event_total = 0
    if current_event_total > 0:
        events.append(current_event_total)
    return events

def main():
    filename = "./weather(146)_2022-2022.csv"
    rainfalls = get_weather_data_int(filename, 9)  # 9번 열이 강수량 열이라고 가정
    rain_event_amounts = get_rain_event_amounts(rainfalls)
    print(f"강우 이벤트 중 최대 강수량은 {max(rain_event_amounts)}mm입니다")

if __name__ == "__main__":
    main()
