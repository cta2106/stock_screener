from parse import parse_stock_file
from rsi import calculate_rsi
import yaml


def main():
    with open("config/stocks.yml") as file:
        config = yaml.full_load(file)

    stocks = config["stocks"]

    for stock_name in stocks:
        stock_df = parse_stock_file(stock_name)

        if stock_df is not None:
            _, _, _, _, closep, _, _ = stock_df.values.tolist()
            latest_rsi_value = calculate_rsi(closep)[-1]

            if latest_rsi_value < 30:
                print("buy {}! rsi value: {}".format(stock_name, latest_rsi_value))

            elif latest_rsi_value > 70:
                print("sell {}! rsi value: {}".format(stock_name, latest_rsi_value))


if __name__ == "__main__":
    main()
