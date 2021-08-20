import yfinance

def stock_data(ticker):
    stock = yfinance.Ticker(ticker)
    info = stock.info
    try:
        result = {
            'NAME': info['shortName'],
            'TICKER': ticker,
            'PRICE_BUY': info['bid'],
            'PRICE_SELL': info['ask'],
            'INFO': info
        }
    except:
        return False
    return result

def check_password(p):
    if len(p) < 7:
        return False
    if len(p) > 20:
        return False
    digits = '1234567890'
    found_int = False
    for dig in digits:
        if dig in p:
            found_int = True
            break
    if not found_int:
        return False
    chars = 'qwertyuiopasdfghjklzxcvbnm'
    found_char = False
    for char in chars:
        if char in p:
            found_char = True
            break
    if not found_char:
        return False
    Chars = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    found_Char = False
    for Char in Chars:
        if Char in p:
            found_Char = True
            break
    if not found_Char:
        return False
    return True


def decode_stocks_dict(stocks):
    result = ''
    for stock,shares in stocks.items():
        result += str(stock) + '!@#$%' + str(shares) + '!@#$%'
    return result