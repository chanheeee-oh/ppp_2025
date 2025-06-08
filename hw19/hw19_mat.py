import pandas as pd
import matplotlib.pyplot as plt

def main():
    filename = "./weather(146)_2005-2005.csv"
    df = pd.read_csv(filename, skipinitialspace=True)

    jan26 = df[(df["month"] == 1) & (df["day"] == 26)].iloc[0]

    data = {
        "Maximum Temperature (tmax)": jan26["tmax"],
        "Snowfall (snow)": jan26["snow"]
    }

    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values(), color=["salmon", "lightblue"])
    plt.title("2005year 1month 26day weather (my birthday!)")
    plt.ylabel("temperature")
    plt.grid(axis='y')
    plt.ylim(min(data.values()) - 2, max(data.values()) + 2)

    plt.show()

if __name__ == "__main__":
    main()

