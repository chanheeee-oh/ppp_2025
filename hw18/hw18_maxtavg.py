import pandas as pd

def get_total_precipitation(filename):
    df = pd.read_csv(filename, encoding="utf-8-sig", skipinitialspace=True)
    df.columns = df.columns.str.strip()

    if "rainfall" in df.columns:
        return df["rainfall"].dropna().sum()
    else:
        print(f"[ERROR] 'rainfall' 컬럼이 없습니다. 실제 컬럼: {df.columns.tolist()}")
        return None

def main():
    filename_suwon = "./weather(119)_2019-2019.csv"
    filename_jeonju = "./weather(146)_2019-2019.csv"

    total_rain_suwon = get_total_precipitation(filename_suwon)
    total_rain_jeonju = get_total_precipitation(filename_jeonju)

    if total_rain_suwon is not None and total_rain_jeonju is not None:
        diff = abs(total_rain_suwon - total_rain_jeonju)
        print(f"2019년 수원시와 전주시의 총강수량 차이는 {diff:.1f}mm입니다.")
    else:
        print("총강수량 데이터를 계산할 수 없습니다.")

if __name__ == "__main__":
    main()


