// Boilerplate JS

// Creating fields in HTML
// https://www.w3schools.com/html/html_forms.asp



// Getting the value of a radio button with JS
// https://stackoverflow.com/questions/9618504/how-to-get-the-selected-radio-button-s-value


// Creating a dropdown menu
// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select

// Getting a dropdown menu selection
// https://stackoverflow.com/questions/1085801/get-selected-value-in-dropdown-list-using-javascript
// https://www.w3schools.com/jsref/prop_select_value.asp

// Using the onclick HTML event/attribute
// https://www.w3schools.com/jsref/event_onclick.asp

// Add text as needed
// https://www.w3schools.com/jsref/met_document_createtextnode.asp

function boilerplateFunction() {
	/* Function to take in user selections and display the necessary text
	
	   The purpose of this function is to utilize the selections that the user made based on dropdowns/radio buttons
	   and display corresponding/necessary text as a result.  


	   Args: N/A
	   Retruns: Returns/displays the user selection(s) for the dropdown(s)/radio button(s)
	   Raises: N/A
	*/

	var genderRadio = document.querySelector("input[name=gender]:checked");
	var genderValue = genderRadio ? genderRadio.value : "";
	console.log(genderValue);

	var selectionRadio = document.querySelector("input[name=selected]:checked");
	var selectionValue = selectionRadio ? selectionRadio.value : "";
	console.log(selectionValue);


	if (selectionValue == "Yes") {

		selectionValue = "This is the FIRST string of text";
	} else {

		selectionValue = "TEST STRING!";
	}

	var selectionDropdown = document.getElementById("genericName");
	var userOutput = selectionDropdown.options[selectionDropdown.selectedIndex].text;
	console.log(userOutput);

	document.getElementById("outputArea").innerHTML = userOutput, selectionValue, genderValue;
	document.getElementById("outputArea").innerHTML = selectionValue;
	document.getElementById("outputArea").innerHTML = genderValue;
	document.getElementById("outputArea").innerHTML = (userOutput + selectionValue + genderValue);

}

/* 
    <h1>Form Demo</h1>
		<form>
		  <input type="radio" name="gender" value="male" checked> Male<br>
		  <input type="radio" name="gender" value="female"> Female<br>
		</form>

	<!-- The second value will be selected initially -->
	<select name="genericName"> 
	  <option value="value1">Value 1</option> 
	  <option value="value2" selected>Value 2</option>
	  <option value="value3">Value 3</option>
	</select>

*/
