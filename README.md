# tradier

simple client to interface with tradier

To install:

`pip install python-tradier`

Simple example:

```
import tradier

t = tradier.Tradier(access_token="your access token")
t.get_lookup("goog")
```

fairly lean right now, only implements a few get methods,
designed to be very easily extensible. Feel free to open a pull request.

to run the tests, do

`pytest`
