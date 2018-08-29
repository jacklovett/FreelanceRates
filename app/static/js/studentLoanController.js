	
window.onload = studentLoanController();

function studentLoanController() {
	
	var row, plan1, plan2, planToggle;
	
	try {
		row = document.getElementById("row");
		planToggle = document.querySelector("input[name=plan_toggle]");
		// radio buttons
		plan1 = document.getElementById("plan_1");
		plan2 = document.getElementById("plan_2");
	} catch(error) {
		console.log(error);
	}
						
	// plan display toggle
	planToggle.onchange = function() {
		try	{
			if(this.checked) {
				plan1.checked = true;
				row.style.display = "";
			}else {
				row.style.display = "none";
				plan1.checked, plan2.checked = false;			
			} 
		}catch(error) {
			console.log(error);
		}
	};
		
	// plan1 radio switch
	plan1.onchange = function() {
		if(this.checked) plan2.checked = false;
	};

	// plan2 radio switch
	plan2.onchange = function() {
		if(this.checked) plan1.checked = false;
	};
	
};

