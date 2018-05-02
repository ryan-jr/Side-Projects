// JS code here

var calculationHolder = []

function showDiv(clickedId) {

	var data = Number(clickedId);
	document.getElementById("window").style.display="";


	// https://stackoverflow.com/questions/4825295/javascript-onclick-to-get-the-id-of-the-clicked-button
	// https://www.w3schools.com/js/js_output.asp
	// https://www.w3schools.com/jsref/jsref_isnan.asp
	// https://stackoverflow.com/questions/2801601/why-does-typeof-nan-return-number
	document.getElementById("window").innerHTML = clickedId;

	if (isNaN(clickedId) === false) {

		console.log(clickedId, "is a number!");
	} else {

		console.log(clickedId, "is Not A Number!");
	}




}


	/* 
	if (document.getElementById("one") == true) {
		console.log("one!");
		var newInput = 1;
		calculationHolder.push(newInput);
	} else if (document.getElementById("two") == true) {
		console.log("two");
		var input = 2;
		calculationHolder.push(input);

	} 

	else if (input === "three") {
		console.log("three");
		input = 3;
		calculationHolder.push(input);

	} else if (document.getElementById("four")) {
		console.log("four");
		input = 4;
		calculationHolder.push(input);
	} else if (document.getElementById("five")) {
		console.log("five");
		input = 5;
		calculationHolder.push(input);
	} else if (document.getElementById("six")) {
		console.log("six");
		input = six;
		calculationHolder.push(input);
	} else if (document.getElementById("seven")) {
		console.log("seven");
		input = 7;
		calculationHolder.push(input);
	} else if (document.getElementById("eight")) {
		console.log("eight");
		input = 8;
		calculationHolder.push(input);
	} else if (document.getElementById("nine")) {
		console.log("nine");
		input = 9;
		calculationHolder.push(input);
	} else if (document.getElementById("zero")) {
		console.log("zero");
		input = 0;
		calculationHolder.push(input);
	}



*/
	
	//console.log(calculationHolder);

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



