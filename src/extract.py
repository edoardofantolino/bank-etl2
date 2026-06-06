import pandas as pd

def extract(path):

    # print("START extraction")

    df = pd.read_csv(path)

    # print("FINISH extraction")

    return df