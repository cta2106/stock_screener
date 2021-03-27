from evaluate import evaluate_stocks
import yaml


def main():
    with open("config/stocks.yml") as file:
        config = yaml.full_load(file)

    stocks = config["stocks"]

    for stock_name in stocks:
        latest_rsi_value = evaluate_stocks(stock_name)

        if latest_rsi_value:

            if latest_rsi_value < 30:
                print("buy {}! rsi value: {}".format(stock_name, latest_rsi_value))

            elif latest_rsi_value > 70:
                print("sell {}! rsi value: {}".format(stock_name, latest_rsi_value))


if __name__ == "__main__":
    main()
