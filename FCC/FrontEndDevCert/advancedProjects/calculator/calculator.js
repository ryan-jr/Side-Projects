// JS code here

var calculationHolder = [];
var numberHolder = "";

// TODO: Access the last element unless it is an operand and add to the string in/at that element
// TODO: If it is an operand, create a new element in the array 
// TODO: Find/create a way to loop through the array and perform calculations
// TODO: With the result of the calculations display them to the screen
// TODO: Make sure that the "=", ends everything else and does stuff

function numberCalculation(clickedId) {


	if (clickedId === "1") {
			console.log("one!");
			var input = 1;
			calculationHolder.push(input);

	}  else if (clickedId === "2") {
		console.log("two");
		var input = 2;
		calculationHolder.push(input);

	} else if (clickedId === "3") {
		console.log("three");
		input = 3;
		calculationHolder.push(input);

	} else if (clickedId === "4") {
		console.log("four");
		input = 4;
		calculationHolder.push(input);

	} else if (clickedId === "5") {
		console.log("five");
		input = 5;
		calculationHolder.push(input);

	} else if (clickedId === "6") {
		console.log("six");
		input = 6;
		calculationHolder.push(input);

	} else if (clickedId === "7") {
		console.log("seven");
		input = 7;
		calculationHolder.push(input);

	} else if (clickedId === "8") {
		console.log("eight");
		input = 8;
		calculationHolder.push(input);

	} else if (clickedId === "9") {
		console.log("nine");
		input = 9;
		calculationHolder.push(input);

	} else if (clickedId === "0") {
		console.log("zero");
		input = 0;
		calculationHolder.push(input);
	} else if (clickedId === "/") {
		console.log("/");
		input = "/";
		calculationHolder.push(input);
	} else if (clickedId === "*") {
		console.log("*");
		input = "*";
		calculationHolder.push(input);
	} else if (clickedId === "+") {
		console.log("+");
		input = "+";
		calculationHolder.push(input);
	} else if (clickedId === "-") {
		console.log("-");
		input = "-";
		calculationHolder.push(input);
	} 

	console.log(calculationHolder);
}


function showDiv(clickedId) {

	var data = Number(clickedId);
	var calcNumber = ""
	document.getElementById("window").style.display="";


	// https://stackoverflow.com/questions/4825295/javascript-onclick-to-get-the-id-of-the-clicked-button
	// https://www.w3schools.com/js/js_output.asp
	// https://www.w3schools.com/jsref/jsref_isnan.asp
	// https://stackoverflow.com/questions/2801601/why-does-typeof-nan-return-number
	document.getElementById("window").innerHTML = clickedId;

	if (isNaN(clickedId) === false) {

		console.log(clickedId, "is a number!");
		numberCalculation(clickedId);

	} else {

		console.log(clickedId, "is Not A Number!");
		numberCalculation(clickedId);
	}



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



