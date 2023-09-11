import pandas as pd

def data_filter(df):
    return df[df[" \"Test3\""] >= 80]


if __name__ == "__main__":
    print(data_filter(pd.read_csv("./grades.csv")))