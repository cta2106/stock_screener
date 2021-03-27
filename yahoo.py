import urllib
from cookie import get_cookie_crumb


def load_yahoo_url(ticker, data_range, info="quote"):
    _cookie, _crumb = get_cookie_crumb()
    param = dict()
    param["range"] = data_range
    param["interval"] = "1d"
    if info == "quote":
        param["events"] = "history"
    elif info == "dividend":
        param["events"] = "div"
    elif info == "split":
        param["events"] = "split"
    param["crumb"] = _crumb
    params = urllib.parse.urlencode(param)
    url = "https://query1.finance.yahoo.com/v7/finance/download/{}?{}".format(
        ticker, params
    )
    return url
