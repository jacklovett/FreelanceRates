	
window.onload = freelanceRates();

function freelanceRates() {
	
	var showInfoView = false;
		
	var planRow = document.getElementById("plan_row");
	var planInfoRow = document.getElementById("plan_info_row");
	var planToggle = document.querySelector("input[name=plan_toggle]");
	var planInfoToggle = document.getElementById("plan_info_toggle");
	// radio buttons
	var plan1 = document.getElementById("plan_1");
	var plan2 = document.getElementById("plan_2");
							
	// plan display toggle
	planToggle.onchange = function() {
		if(this.checked) {
			plan1.checked = true;
			planRow.style.display = "";
		}else {
			planRow.style.display = "none";
			plan1.checked, plan2.checked = false;			
		} 		
	};

	// plan info display toggle
	planInfoToggle.onclick = function() {
		showInfoView = !showInfoView
		if(showInfoView) 
			planInfoRow.style.display = "";
		else 
			planInfoRow.style.display = "none";	
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

