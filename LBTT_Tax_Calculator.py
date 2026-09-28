"""
https://gitlab.com/iamemc/lbtt_tax_calculator

LBTT rates and bands for residential transactions as of 1 April 2021:
    Purchase price 	 LBTT rate
    
    Up to £145,000          0%
    £145,001 to £250,000    2%
    £250,001 to £325,000    5%
    £325,001 to £750,000    10%
    Over £750,000           12%
 
Source: https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property#residential%20property%20rates%20and%20bands 
"""
import locale
import math
import csv
import os
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

########## Get LBTT Bands and Rates
def getLBTTBandsAndRates():
    """
    getLBTTBandsAndRates: clears all non numeric characters in a string of integers
        Args: NONE
    
        Returns:
            LBTT_bands_and_rates (DICT) : A dictionary containing all tax bands and rates
    """
    if os.path.exists('LBTT_bands_and_rates.csv'):
        with open('LBTT_bands_and_rates.csv') as csv_file:
            reader = csv.reader(csv_file)
            LBTT_bands_and_rates = {}
            for row in reader:
                row = row[0].split(';')
                LBTT_bands_and_rates[str(row[0])] = int(row[-1])
    else:
        LBTT_bands_and_rates = {
            '145,000': 0,
            '250,000': 2,
            '325,000': 5,
            '750,000': 10,
            '>750,000': 12,
            }
    return LBTT_bands_and_rates

def numericStringCleaner(string):
    """
    numericStringCleaner: clears all non numeric characters in a string of integers
        Args:
            string (STR): Any string
    
        Returns:
            cleaned_string (INT) : An Integer from the previous string.
    """
    cleaned_string = ''
    for i in string:
        if i.isnumeric():
            cleaned_string += i

    return int(cleaned_string)

def taxCalculator(property_value, LBTT_bands_and_rates):
    """
    taxCalculator: Computes the sum of several tax brackets and their respective
                    tax percentage.
        Args:
            property_value (INT) : A number representing a property sale value.
            LBTT_bands_and_rates (DICT): Government established rates and bands.
                        Last index assumes infinite upper bound.

        Returns:
            total_taxes (list): the sum of all taxes per bracket.
    """
    taxes_per_bracket = []
    for i in range(0, len(LBTT_bands_and_rates)):
        tax_band_upper_bound = \
            numericStringCleaner(list(LBTT_bands_and_rates.keys())[i])
        tax_band_lower_bound = \
            (numericStringCleaner(list(LBTT_bands_and_rates.keys())[i- 1]) 
             if i != 0 else 0) 

        # Checks if there's a lower and upper bound (useful because of >N),
        #   if so, checks if there's still property value in a tax bracket.
        # The comparison is because the difference between (upper - lower)
        #   bounds is always lower than (property value - upper_bound) until
        #   >N is reached (see below).
        # If any subtraction is negative returns 0 -> no more bracket tax
        #   can be paid except for >N.
        if tax_band_upper_bound > tax_band_lower_bound:
            amount_in_tax_band = max(min(tax_band_upper_bound - tax_band_lower_bound, \
                                         property_value - tax_band_lower_bound),0)

        # If both bounds are the same, we can assume:
        #   |X up to Z|
        #   |Z up to N| lower bound -> N
        #   |   > N   | upper bound -> N
        # Thus N = N, since > N is the last tier (any property value higher
        #   than N), we only need to get the tax of the difference between
        #   the property value and the upper bound and get its value.
        else:
            amount_in_tax_band = property_value - tax_band_upper_bound

        taxes_per_bracket.append(int(list(LBTT_bands_and_rates.values())[i]) \
                                         * amount_in_tax_band / 100)

        # If property_value is lower than the Upper Bound we don't need to 
        #   continue the iteration as there will never be any value higher
        #   than the higher tax bracket and the property value itself.
        if property_value < tax_band_upper_bound:
            break

    return math.floor(sum(taxes_per_bracket))


def driverCode():
    LBTT_bands_and_rates = getLBTTBandsAndRates()
    print(f"Amount of LBTT tax to pay: {locale.currency(taxCalculator(10000000, LBTT_bands_and_rates), grouping=True)}")


driverCode()