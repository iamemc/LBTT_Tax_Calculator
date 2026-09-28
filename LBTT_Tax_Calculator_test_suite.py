import LBTT_Tax_Calculator
import unittest

"""
EXPECTED RESULTS TAKEN FROM:
    https://revenue.scot/calculate-tax/calculate-property-transactions#calculator
"""

LBTT_bands_and_rates = LBTT_Tax_Calculator.getLBTTBandsAndRates()

#================ Test Class  ====================
class testSuite(unittest.TestCase):

####### taxCalculator
    """
    taxCalculator: Computes the sum of several tax brackets and their respective
                    tax percentage.
    """
    #test1
    def test_1Million(self):
        actual = 1000000
        expected = 78350
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test2
    def test_1Pound(self):
        actual = 1
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test3 - FREE HOUSE
    def test_Free(self):
        actual = 0
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test4 - EDGE CASE LOWER & UPPER BOUND
    def test_LowerBound1(self):
        actual = 145000
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test5 - EDGE CASE LOWER & UPPER BOUND
    def test_LowerBound1PlusOne(self):
        actual = 145001
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test6 - EDGE CASE LOWER & UPPER BOUND
    def test_LowerBound2Minus1(self):
        actual = 149999
        expected = 99
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test7 - EDGE CASE LOWER & UPPER BOUND
    def test_LowerBound2(self):
        actual = 150000
        expected = 100
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test8 - EDGE CASE LOWER & UPPER BOUND
    def test_LowerBound2Plus1(self):
        actual = 150001
        expected = 100
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test9 - NEGATIVE
    def test_Negative(self):
        actual = -100000
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test10 - Normal
    def test_Normal(self):
        actual = 354054
        expected = 8755
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test11
    def test_BuckinghamPalace(self):
        actual = 49000000
        expected = 5838350
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test12
    def test_testRoundCalc(self):
        actual = 145050
        expected = 1 #
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

    #test12
    def test_testRoundCalc2(self):
        actual = 145049
        expected = 0 #even though tax should be £0.98 it gets rounded to 0
        self.assertEqual(LBTT_Tax_Calculator.taxCalculator(actual, LBTT_bands_and_rates), expected)

####### numericStringCleaner
    """
    numericStringCleaner: clears all non numeric characters in a string.
    """
    #test1
    def test_Clean_Numeric_String(self):
        actual = '4a9b0c0d0e0f0g0'
        expected = 49000000
        self.assertEqual(LBTT_Tax_Calculator.numericStringCleaner(actual), expected)
    #test2
    @unittest.expectedFailure
    def test_Clean_Numeric_String_No_Digit(self):
        actual = 'x'
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.numericStringCleaner(actual), expected)
    #test3
    def test_Clean_Numeric_String_Foreign_Alphabet(self):
        actual = '᠀᠋ᠳᠠᠷᠬᠠᠨ ᠮᠠᠨ ᠤ 99ᠲᠤᠰᠠᠭᠠᠷ ᠤᠯᠤᠰ'
        expected = 99
        self.assertEqual(LBTT_Tax_Calculator.numericStringCleaner(actual), expected)
    #test4
    def test_Clean_Numeric_String_Cyrillic(self):
        actual = 'Монг2ол Улсын1 төрийн дуулал'
        expected = 21
        self.assertEqual(LBTT_Tax_Calculator.numericStringCleaner(actual), expected)
    #test5
    def test_Clean_Numeric_String_Os(self):
        actual = 'Ø0O'
        expected = 0
        self.assertEqual(LBTT_Tax_Calculator.numericStringCleaner(actual), expected)
        
unittest.main(argv=['first-arg-is-ignored'], exit=False)