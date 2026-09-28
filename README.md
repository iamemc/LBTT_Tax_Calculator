# LBTT (Land and Buildings Transaction Tax) Tax Calculator



## 🧮 LBTT Tax Calculator

<p align="center">
  <a href="https://iamemc.github.io/LBTT_Tax_Calculator/">
    <img src="./use-tool.png" alt="Use the LBTT Tax Calculator" width="800">
  </a>
</p>



## What is LBTT?

Land and Buildings Transaction Tax (LBTT) is a Scottish tax applied to residential and commercial land and buildings transactions. It replaced UK Stamp Duty Land Tax (SDLT) in Scotland from 1 April 2015.

LBTT is designed so that the charge is more proportionate to the actual price of the property, with different rates and bands for different types of properties. For residential properties, LBTT applies progressive tax rates based on the purchase price:

- **Up to £145,000**: 0% tax
- **£145,001 to £250,000**: 2% tax
- **£250,001 to £325,000**: 5% tax
- **£325,001 to £750,000**: 10% tax
- **Over £750,000**: 12% tax

The structure ensures that tax is only applied to portions of the purchase price that fall within each band, making it more proportionate to the actual property value.

## What This Calculator Does

This Python application calculates the total Land and Buildings Transaction Tax (LBTT) amount for property transactions in Scotland based on the current tax bands and rates. The calculator:

- Implements progressive tax calculation across multiple bands
- Handles edge cases including free properties, negative values, and boundary conditions
- Uses the specific LBTT tax bands as of 1 April 2021
- Provides accurate tax calculations for property purchase values
- Includes unit tests to verify the accuracy of calculations

## How to Use

To run the calculator:

1. Ensure you have Python installed on your system
2. Run the main script:
   ```bash
   python LBTT_Tax_Calculator.py
   ```

The application will output the calculated LBTT tax for a test property value (currently set to £10,000,000).

## Tax Bands and Rates

The calculator uses the following progressive tax bands:

- **£0 to £145,000**: 0% tax
- **£145,001 to £250,000**: 2% tax  
- **£250,001 to £325,000**: 5% tax
- **£325,001 to £750,000**: 10% tax
- **Over £750,000**: 12% tax

## Testing

The calculator includes a comprehensive test suite (`LBTT_Tax_Calculator_test_suite.py`) that validates:
- Basic functionality with various property values
- Edge cases including boundary conditions
- Free properties (value of £0)
- Negative values
- Large property values
- Round-off behavior

To run the tests, execute:
```bash
python LBTT_Tax_Calculator_test_suite.py
```

## Features

- **Progressive Tax Calculation**: Accurately calculates tax across multiple bands
- **CSV Support**: Can read tax bands from a CSV file or use default values
- **Error Handling**: Handles edge cases appropriately
- **Unit Tests**: Comprehensive test coverage to ensure accuracy
- **Internationalization**: Uses proper currency formatting for Scottish pounds

## Requirements

- Python 3.x

## Author

Eduardo Carvalho | 2022


## License

This project is licensed under the MIT License - see the LICENSE file for details.
