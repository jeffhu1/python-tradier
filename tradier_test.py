import calendar
import datetime

import pytest

from tradier import Tradier

ACCESS_TOKEN = "your access token"
TODAY = datetime.date.today()
FRIDAY = TODAY + datetime.timedelta((calendar.FRIDAY - TODAY.weekday()) % 7)


def test_fake_access_token():
    t = Tradier(access_token="Not a real access token")
    with pytest.raises(AssertionError):
        t.get_lookup("goog")


def test_get_quotes():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_quotes(symbols="AAPL")
    assert result["quotes"] != None


def test_get_options_chains():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_options_chains(symbol="VXX", expiration=str(FRIDAY), greeks="true")
    assert result["options"] != None


def test_get_options_strikes():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_options_strikes(symbol="VXX", expiration=str(FRIDAY))
    assert result["strikes"] != None


def test_get_options_expirations():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_options_expirations(symbol="VXX")
    assert result["expirations"] != None


def test_get_lookup_options_symbols():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_lookup_options_symbols(underlying="SPY")
    assert result["symbols"] != None
    assert len(result["symbols"][0]["options"]) > 0


def test_get_history():
    expected = {
        "history": {
            "day": {
                "date": "2019-05-06",
                "open": 1166.26,
                "high": 1190.85,
                "low": 1166.26,
                "close": 1189.39,
                "volume": 1563943,
            }
        }
    }
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_history(
        symbol="goog", interval="daily", start="2019-05-04", end="2019-05-06"
    )
    assert result == expected


def test_get_timesales():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_timesales(symbol="AAPL", interval="15min")
    assert result["series"] != None


def test_get_etb():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_etb()
    assert result["securities"] != None
    assert len(result["securities"]["security"]) > 0


def test_get_clock():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_clock()
    assert result["clock"] != None


def test_get_calendar():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_calendar()
    assert result["calendar"] != None


def test_get_search():
    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_search(q="alphabet")
    assert result["securities"] != None
    assert len(result["securities"]["security"]) > 0


def test_get_lookup():
    expected = {
        "securities": {
            "security": {
                "symbol": "GOOGL",
                "exchange": "Q",
                "type": "stock",
                "description": "Alphabet Inc",
            }
        }
    }

    t = Tradier(access_token=ACCESS_TOKEN)
    result = t.get_lookup("googl")
    assert result == expected
