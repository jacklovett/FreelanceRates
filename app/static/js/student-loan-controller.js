	
window.onload = studentLoanController();

function studentLoanController() {
	
	var showInfoView = false;
		
	var planRow = document.getElementById("plan-row");
	var planInfoRow = document.getElementById("plan-info-row");
	var hasStudentLoan = document.querySelector("input[name=has-student-loan]");
	var planInfoToggle = document.getElementById("plan-info-toggle");
	// radio buttons
	var plan1 = document.getElementById("plan-1");
	var plan2 = document.getElementById("plan-2");
							
	// plan display toggle
	hasStudentLoan.onchange = function() {
		try {
			if(this.checked) {
				plan1.checked = true;
				planRow.style.display = "";
			}else {
				planRow.style.display = "none";
				plan1.checked, plan2.checked = false;			
			} 	
		} catch (error) {
			console.log(error);
		}	
	};

	// plan info display toggle
	planInfoToggle.onclick = function() {
		try {
			showInfoView = !showInfoView
			if(showInfoView) 
				planInfoRow.style.display = "";
			else 
				planInfoRow.style.display = "none";	
		} catch (error) {
			console.log(error);
		}
	}
		
	// plan1 radio switch
	plan1.onchange = function() {
		if(this.checked) plan2.checked = false;
	};

	// plan2 radio switch
	plan2.onchange = function() {
		if(this.checked) plan1.checked = false;
	};
	
};

