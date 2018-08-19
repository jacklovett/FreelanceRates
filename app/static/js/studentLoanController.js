	
window.onload = studentLoanController();

function studentLoanController() {
	try	{
		var row = document.getElementById("row");
		var planToggle = document.querySelector("input[name=plan-toggle]");
		    	
		planToggle.onchange = function() {
			if(this.checked)
				row.style.display = "";				
			else 
				row.style.display = "none";								
		};
	} catch(error) {
		console.log(error);
	}
};
