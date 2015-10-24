# Reddit Currency Bot
Reddit bot that parses submission titles for currency values using [currency conversion library](https://github.com/cp2846/currency-converter) for Python.
If a match is found, it replies with up-to-date exchange rates for that currency. Exchange rates are taken from the [fixer.io API](http://fixer.io).

The script will look for a text file in the working directory named posts_replied_to.txt in which to save processed posts. If no such file exists, it will store the values in a temporary list.

# Dependencies
[Praw](https://github.com/praw-dev/praw)

[OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util)

[currencyconverter](https://github.com/cp2846/currency-converter)
