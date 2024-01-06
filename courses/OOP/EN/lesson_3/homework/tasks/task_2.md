## Currency Converter

If you take a look at the [file](https://www.floatrates.com/daily/mdl.json)
You will see a very long list of all currencies and their conversion rate from and to MDL.

## Task

Create a program that is going to load this list into the program.

On program start-up, show the list of all possible conversions, with rates from lowest to highest.

Let the user input the name of the currency to convert to. Example: EUR or MDL

* If the input currency is MDL, then use the ask the user to input again what currency to convert to MDL. Example USD
    * Let the user input the value of MDL to convert to that currency.
    * Print the converted value with only 2 decimal points (example 92.43)
* If the input currency is not MDL, then:
    * Let the user input the value of MDL to convert to that currency.

## Conditions

* The entire program should be object-oriented (only use classes), except for the main.py which will run the program
* You should create CurrencyConversion object, that will store all information about each conversion.
    * Example:
    * CurrencyConversion(from="MDL", to="EUR", rate=19.230137733112, name="MDL -> EUR")
    * CurrencyConversion(from="EUR", to="MDL", rate=0.052001707625739, name="EUR -> MDL")
* In order to have the ability to sort CurrencyConversion objects, implement the `__lt__, __eq__` functions. These
  functions should compare the rates of the CurrencyConversion objects.
* Have a CurrencyConversionService that will store and manage all the currency conversion information, and should have
  at least this method below.
    * convert(from_currency, to_currency, amount)
* In cases of issues (for example the conversion is not possible or conversion data is missing) you must raise the
  appropriate exception.
* Add other objects and classes as you see fit, and make your program run using the example code below:

```python
conversion_data = ConversionFileService.load_from_file('filename.json')
# conversion_data = ConversionFileService.load_from_url('link/to/floatrates/conversions') # You could also implement loading from the web site as well

converter = CurrencyConversionService(conversion_data)
amount_in_eur = converter.convert("MDL", "EUR", 2000)
rate_eur = converter.get_rate_for("MDL", "EUR")  # Gets rate of conversion from MDL to EUR
```

## Considerations

The json contains a dict of dicts. It's not a list, so pay attention, and analyze the data you are working with before
you start.
