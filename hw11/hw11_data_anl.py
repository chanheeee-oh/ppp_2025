def get_weather_data(filename):
    weather_dates = []
    tmax_list = []
    tmin_list = []
    tavg_list = []

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()


        for line in lines[1:]:
            tokens = line.strip().split(',')

           
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            weather_dates.append([year, month, day])


            if tokens[3] == '':
                tmax_list.append(-999.0)
            else:
                tmax_list.append(float(tokens[3]))

            if tokens[5] == '':
                tmin_list.append(-999.0)
            else:
                tmin_list.append(float(tokens[5]))

            if tokens[4] == '':
                tavg_list.append(-999.0)
            else:
                tavg_list.append(float(tokens[4]))

    return weather_dates, tmax_list, tmin_list, tavg_list


def main():
    filename = "./weather(146)_2001-2022.csv"
    dates, tmax, tmin, tavg = get_weather_data(filename)

    print("\n연도별 최대 일교차:")

    for year in range(2001, 2023):
        max_gap = -1000.0
        max_month = 0
        max_day = 0

        for i in range(len(dates)):
            y, m, d = dates[i]

            if y == year:
                if tmax[i] != -999.0 and tmin[i] != -999.0:
                    gap = tmax[i] - tmin[i]
                    if gap > max_gap:
                        max_gap = gap
                        max_month = m
                        max_day = d

        print(f"{year}/{max_month:02d}/{max_day:02d} {max_gap:.1f}")

    print("\n연도별 5-9월 적산온도:")

    for year in range(2001, 2023):
        gdd_sum = 0.0

        for i in range(len(dates)):
            y, m, d = dates[i]

            if y == year and 5 <= m <= 9:
                if tavg[i] != -999.0:
                    if tavg[i] > 5:
                        gdd_sum += (tavg[i] - 5)

        print(f"{year} {gdd_sum:.1f}")


if __name__ == "__main__":
    main()



