// LBTT Tax Calculator - Optimized Implementation

const LBTT_BANDS_AND_RATES = [
    { upper_bound: 145000, rate: 0 },
    { upper_bound: 250000, rate: 2 },
    { upper_bound: 325000, rate: 5 },
    { upper_bound: 750000, rate: 10 },
    { upper_bound: Infinity, rate: 12 }
];

function calculateLBTT(property_value) {
    if (property_value <= 0) return 0;
    
    let total_tax = 0;
    let remaining_value = property_value;
    let previous_bound = 0;
    
    for (let i = 0; i < LBTT_BANDS_AND_RATES.length; i++) {
        const band = LBTT_BANDS_AND_RATES[i];
        let taxable_amount;
        
        if (i === LBTT_BANDS_AND_RATES.length - 1) {
            taxable_amount = Math.max(0, remaining_value - previous_bound);
        } else {
            const current_bound = band.upper_bound;
            taxable_amount = Math.max(0, Math.min(current_bound, property_value) - previous_bound);
        }
        
        total_tax += (taxable_amount * band.rate) / 100;
        previous_bound = band.upper_bound;
        
        if (remaining_value <= band.upper_bound) break;
    }
    
    return Math.floor(total_tax);
}

function formatCurrency(amount) {
    return "£" + amount.toLocaleString("en-GB");
}

function handleFormSubmit(event) {
    event.preventDefault();
    
    const propertyValueInput = document.getElementById('propertyValue');
    const propertyValue = parseFloat(propertyValueInput.value);
    
    if (isNaN(propertyValue) || propertyValue < 0) {
        alert("Please enter a valid positive number for property value.");
        return;
    }
    
    const lbttTax = calculateLBTT(propertyValue);
    
    document.getElementById('taxResult').textContent = `The calculated LBTT tax is: ${formatCurrency(lbttTax)}`;
    document.getElementById('propertyValueDisplay').textContent = formatCurrency(propertyValue);
    document.getElementById('taxAmountDisplay').textContent = formatCurrency(lbttTax);
    
    const resultContainer = document.getElementById('result');
    resultContainer.style.display = 'block';
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('taxCalculator');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
    
    // Set up example value
    document.getElementById('propertyValue').value = 1000000;
});