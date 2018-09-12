window.onload = currencyFormatter();

function currencyFormatter() {
    // edit so that this also works with focus on salary input field
    const formatter = new Intl.NumberFormat('en-GB', {
        style: 'currency',
        currency: 'GBP',
        minimumFractionDigits: 2
      });

    var currencyElements = document.getElementsByClassName('currency');
    
    var formatCurrency = function(currency){
        try {
            currencyValue = currency.innerHTML;
            if(currencyValue != "") 
                currency.innerHTML = formatter.format(currencyValue);
        } catch (error) {
            console.log(error);
        }
    } 

    for(var i=0; i<currencyElements.length; i++) {
        formatCurrency(currencyElements[i]);
    }

};