def get_weather_data_int(filename, col_idx):
    weather_datas = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[col_idx] != "":
                weather_datas.append(int(float(tokens[col_idx])))

    return weather_datas

def get_rain_events(rainfalls):
    events = []
    continued_rainday = 0
    for rain in rainfalls:
        if rain > 0:
            continued_rainday += 1
        else:
            if continued_rainday > 0:
                events.append(continued_rainday)
                continued_rainday = 0
    if continued_rainday > 0:
        events.append(continued_rainday)
    return events

def main():
    filename = "./weather(146)_2022-2022.csv"
    rainfalls = get_weather_data_int(filename, 9)
    events = get_rain_events(rainfalls)
    print(f"최장연속강우일수 = {max(events)}일")

if __name__ == "__main__":
    main()

