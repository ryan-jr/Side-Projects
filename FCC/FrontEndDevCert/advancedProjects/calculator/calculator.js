// JS code here

var calculationHolder = [];
var numberHolder = "";
var clickedString = "";
var finalResult = "";

// TODO: Access the last element unless it is an operand and add to the string in/at that element (COMPLETE)
// TODO: If it is an operand, create a new element in the array (COMPLETE)
// TODO: Find/create a way to loop through the array and perform calculations (COMPLETE/Eval)
// TODO: With the result of the calculations display them to the screen (IN PROGRESS)
// TODO: Make sure that the "=", ends everything else and does stuff (IN PROGRESS)
// TODO: Update it so that operands display to the calculation window (this is a result of how you add an empty element after an operand)
// TODO: Display the final result to the window (Clear the array after the eval add the result to it, display it, and then clear the array again?)



// Make it so that numbers push onto the array and operands push onto the array their operand AND an empty string
// That way if a numberString needs to be concatenated/added onto it can be added to the array by replacing the last element
// And this makes it so that the last element after an operand is NOT the operand itself

function calculationLoop(calculationArr) {
	// Function to calculation the numbers/operands contained in the array
	// Args: 
	//		calculationArr: Array of strings that are either integers or operands
	// Returns:
	//		finalResult: String of the result of the calculation
	// Raises:
	//		N/A
	console.log("Function!!!");
	var tempHolder1 = 0;
	console.log(calculationArr.length);
	tempHolder1 = eval(calculationHolder.join(" "));
	// https://stackoverflow.com/questions/13077923/how-can-i-convert-a-string-into-a-math-operator-in-javascript
	return tempHolder1;

}

function numberCalculation(clickedId) {

	// Checking to make sure the array isn't empty first (and that it exists)
	// https://stackoverflow.com/questions/24403732/check-if-array-is-empty-does-not-exist-js/24403771
	// https://www.w3schools.com/jsref/jsref_push.asp


	// Pass block if = so we don't add it to the calculation string
	if (clickedId === "=") {
		

	} else {

		clickedString += clickedId;
	}
	
	// I could probably refactor this to just do things if 
	if (calculationHolder === undefined || calculationHolder.length == 0) {
    		calculationHolder.push("zzz");

	}	else if (clickedId === "1") {
			console.log("one!");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);



	}  else if (clickedId === "2") {
			console.log("two");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);


	} else if (clickedId === "3") {
			console.log("three");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "4") {
			console.log("four");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "5") {
			console.log("five");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "6") {
			console.log("six");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "7") {
			console.log("seven");
		 	console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "8") {
			console.log("eight");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "9") {
			console.log("nine");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "0") {
			console.log("zero");
			console.log(calculationHolder);
			calculationHolder.pop();
			calculationHolder.push(clickedString);
			console.log(calculationHolder);

	} else if (clickedId === "/") {
			console.log("/");
			input = "/";
			calculationHolder.push(input);
			calculationHolder.push("");
			clickedString = "";

	} else if (clickedId === "*") {
			console.log("*");
			input = "*";
			calculationHolder.push(input);
			calculationHolder.push("");
			clickedString = "";

	} else if (clickedId === "+") {
			console.log("+");
			input = "+";
			calculationHolder.push(input);
			calculationHolder.push("");
			clickedString = "";

	} else if (clickedId === "-") {
			console.log("-");
			input = "-";
			calculationHolder.push(input);
			calculationHolder.push("");
			clickedString = "";
	}

	if (clickedId === "=") {
		console.log("Equals!");
		clickedString = "";
		finalResult = calculationLoop(calculationHolder);
		console.log(finalResult, "returned!");
		document.getElementById("window").innerHTML = finalResult;
		calculationHolder.length = 0;
	} 


	console.log(calculationHolder);
	console.log(calculationHolder[0]);

	if (calculationHolder[0] === "zzz") {
		console.log(calculationHolder.shift());
		calculationHolder.push(clickedString);

	}

	console.log(calculationHolder);
}


function showDiv(clickedId) {

	var data = Number(clickedId);
	var calcNumber = ""
	document.getElementById("window").style.display="";



	

	if (isNaN(clickedId) === false) {

		console.log(clickedId, "is a number!");
		numberCalculation(clickedId);
		document.getElementById("window").innerHTML = calculationHolder[calculationHolder.length - 1];

	} else {

		console.log(clickedId, "is Not A Number!");
		numberCalculation(clickedId);
		document.getElementById("window").innerHTML = calculationHolder[calculationHolder.length - 2];
	}

	if (finalResult != "") {

		document.getElementById("window").innerHTML = finalResult;
		finalResult = "";
	}

	// https://stackoverflow.com/questions/4825295/javascript-onclick-to-get-the-id-of-the-clicked-button
	// https://www.w3schools.com/js/js_output.asp
	// https://www.w3schools.com/jsref/jsref_isnan.asp
	// https://stackoverflow.com/questions/2801601/why-does-typeof-nan-return-number
	

}
	




	
	

/*
	for(i = 0; i < calculationHolder.length; i++) {
		console.log("Hello");
		document.getElementById("window").innerHTML = calculationHolder;
		
	}
*/




function total() {
	// Function to total everything in the calculationHolder array
	// Stub function for now

}



