import urllib.request, urllib.error, urllib.parse


def _build_cookie_handler():
    cookier = urllib.request.HTTPCookieProcessor()
    opener = urllib.request.build_opener(cookier)
    urllib.request.install_opener(opener)

    _cookie = None
    _crumb = None
    _headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"
    }
    return cookier, _cookie, _crumb, _headers


def get_cookie_crumb():
    cookier, _cookie, _crumb, _headers = _build_cookie_handler()
    cookier.cookiejar.clear()
    req = urllib.request.Request(
        "https://finance.yahoo.com/quote/^GSPC", headers=_headers
    )
    f = urllib.request.urlopen(req, timeout=5)
    alines = f.read().decode("utf-8")

    # Extract the crumb from the response
    cs = alines.find("CrumbStore")
    cr = alines.find("crumb", cs + 10)
    cl = alines.find(":", cr + 5)
    q1 = alines.find('"', cl + 1)
    q2 = alines.find('"', q1 + 1)
    crumb = alines[q1 + 1 : q2]
    _crumb = crumb

    for c in cookier.cookiejar:
        if c.domain != ".yahoo.com":
            continue
        if c.name != "B":
            continue
        _cookie = c.value

    return _cookie, _crumb
