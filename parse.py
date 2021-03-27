from yahoo import load_yahoo_url
import urllib
import numpy as np
import codecs
import datetime
import matplotlib.dates as mdates
import pandas as pd


def parse_stock_file(stock: str):
    url_to_visit = load_yahoo_url(stock, "10y", info="quote")
    stock_file = []
    try:
        source_code = urllib.request.urlopen(url_to_visit).read().decode()
        split_source = source_code.split("\n")
        for eachLine in split_source:
            split_line = eachLine.split(",")
            if len(split_line) == 7:
                if "values" not in eachLine:
                    stock_file.append(eachLine)

        records = np.genfromtxt(
            stock_file,
            delimiter=",",
            unpack=True,
            converters={
                0: lambda s: datetime.datetime.strptime(
                    codecs.decode(s, "UTF-8"), "%Y-%m-%d"
                )
            },
            skip_header=True,
        )
        df = pd.DataFrame.from_records(records)
        df.iloc[:, 0] = df.iloc[:, 0].apply(mdates.date2num)
        return df

    except Exception:
        return None
