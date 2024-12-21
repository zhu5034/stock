# https://ranaroussi.github.io/yfinance/index.html

import yfinance as yf
import sys

if __name__ == '__main__':
    code = sys.argv[1]
    period = sys.argv[2]
    T = yf.Ticker(code)
    res = T.history(period=period)
    print(res)
