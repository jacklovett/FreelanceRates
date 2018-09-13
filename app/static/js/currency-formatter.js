    const formatter = new Intl.NumberFormat('en-GB', {
        style: 'currency',
        currency: 'GBP',
        minimumFractionDigits: 2
    });    
        
    var formatTextCurrency = function() {
        var currencyElements = document.getElementsByClassName('currency');
        for(var i=0; i<currencyElements.length; i++) {
            currencyElements[i].innerHTML = formatCurrency(currencyElements[i].innerHTML);
        }
    }
    
    var formatCurrency = function(value){
        try {
            if(value) 
                return formatter.format(value);
        } catch (error) {
            console.log(error);
        }
    } 

    var formatInputCurrency = function() {
        try {    
            var currencyInput = document.querySelector("input[name=salary]");
            currencyInput.value = formatCurrency(currencyInput.value);
        } catch (error) {
            console.log(error);
        }    
    }; 

 window.onload = formatTextCurrency();
