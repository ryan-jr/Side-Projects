# You don't know JS notes


### Starting Out

* a = b * 2;

* The above is a statement that contains operators(=, *), variables(a, b), literal value(2), and the ending semicolon.

* Statments are made up of expressions which are references to variables/values.  2 in this instance is a literal value expression, b is a variable expression, b * 2 is an arithmetnic expression, a = b * 2 is an assignment expression.  

* An expression statement by itself isn't very useful (such as: b * 2;), because it generally doesn't have any effect.  

* More common expressions are 'call expressions': alert(a);

* JS is generally considered to be interpreted b/c JS code is processed each time it's run, but in reality the JS engine compiles the program on the fly and runs the compiled code.  

* JS is usually printed with console.log("statement goes here");


### Input

* The most common way for JS to get input is for the HTML page to show form elements(text boxes, etc...) for a user to interact with, and then JS reads those values into the program variables.  

* If you're interacting w/ the console the way to get information can be with the prompt method/command:

```javascript

age = prompt( "Please tell me your age:" );

console.log( age );

```

* JS has pretty standard operators +, -, *, /, etc...

* The keyword var is used to declare variables in every program and you should declare/create variables before you use them.



* Common JS operators:

```

Assignment: = as in a = 2.

Math: + (addition), - (subtraction), * (multiplication), and / (division), as in a * 3.

Compound Assignment: +=, -=, *=, and /= are compound operators that combine a math operation with assignment, as in a += 2 (same as a = a + 2).

Increment/Decrement: ++ (increment), -- (decrement), as in a++ (similar to a = a + 1).

Object Property Access: . as in console.log().

Objects are values that hold other values at specific named locations called properties. obj.a means an object value called obj with a property of the name a. Properties can alternatively be accessed as obj["a"]. See Chapter 2.

Equality: == (loose-equals), === (strict-equals), != (loose not-equals), !== (strict not-equals), as in a == b.

See "Values & Types" and Chapter 2.

Comparison: < (less than), > (greater than), <= (less than or loose-equals), >= (greater than or loose-equals), as in a <= b.

See "Values & Types" and Chapter 2.

Logical: && (and), || (or), as in a || b that selects either a or b.

These operators are used to express compound conditionals (see "Conditionals"), like if either a or b is true.

```

### Values and Types

* Primitive values include number(s), string(s), and boolean(s).

* Values that are included directly in the source code are known as literals, with string literals being surrounded by double or single quotes.  

* If you have a number and want to print it on the screen you need to convert the value to a string.  This process in JS is known as coercion.  

```Javascript
// An example of converting a string to a number

var a = "42";
var b = Number( a );

console.log( a );	// "42"
console.log( b );	// 42

```


#### WARNING!!!

* JS will implicitly convert types, which may cause unintended consequences!!!


```

a controversial topic is what happens when you try to compare two values that are not already of the same type, which would require implicit coercion.

When comparing the string "99.99" to the number 99.99, most people would agree they are equivalent. But they're not exactly the same, are they? It's the same value in two different representations, two different types. You could say they're "loosely equal," couldn't you?

To help you out in these common situations, JavaScript will sometimes kick in and implicitly coerce values to the matching types.

So if you use the == loose equals operator to make the comparison "99.99" == 99.99, JavaScript will convert the left-hand side "99.99" to its number equivalent 99.99. The comparison then becomes 99.99 == 99.99, which is of course true.

While designed to help you, implicit coercion can create confusion if you haven't taken the time to learn the rules that govern its behavior. Most JS developers never have, so the common feeling is that implicit coercion is confusing and harms programs with unexpected bugs, and should thus be avoided. It's even sometimes called a flaw in the design of the language.

However, implicit coercion is a mechanism that can be learned, and moreover should be learned by anyone wishing to take JavaScript programming seriously. Not only is it not confusing once you learn the rules, it can actually make your programs better! The effort is well worth it.


```


### Commenting

* Comments should explain why, not what.

* Try and comment just the 'right' amount (i.e. not too much)

* Don't go to the other extreme and leave no comments.  

```Javascript

// Single line comment

/* Multi 
	line
	comment */

```


### Variables

* In the debate between static/strongly enforced typing and weak/dynamic typing, JS falls on the latter side of that debate and uses dynamic typing.  

* The only thing an newly intialized variable needs in front of it is the var keyword.


```Javascript

// Notice the type conversion and the string concat/addition

var a = 22;
console.log("$" + String(a) + ".00");


// $22.00

```

* The fancy word for variables keeping track of changing/updating values is 'state'

* Variables that you intend to keep the same and not change are constants


```Javascript
// Note that constant variables are in caps

var TAX_RATE = 0.08;	// 8% sales tax

var amount = 99.99;

amount = amount * 2;

amount = amount + (amount * TAX_RATE);

console.log( amount );				// 215.9784
console.log( amount.toFixed( 2 ) );	// "215.98"

```

* NOTE: CONSTANT variables are in caps by convention


* The latest version of JS (ES6) declares constants with const and then ALLCAPVARNAME

### Blocks

* Blocks are generally attached to loops, etc... Blocks can be standalone, but isn't usually seen.  

* Note that blocks are defined with opening ({) and closing (}) brackets: {CODE GOES HERE}

```Javascript

// General block:
{
	console.log("Hello world!")
}

// Decision tree block

if (a > 1) {
	console.log("Hello!")
}

### Conditionals

* The most straightforward conditional is the if statment which is equivalent to saying "IF a given condition is true, do the following thing..."

```Javascript

var x = 10;

if (x < 100) {
	
	console.log("x is less than 100!");
}

// x is less than 100!
```

* If you want a backup in case the given condition isn't true you can use an else clause:

```Javascript

var x = 10;

// Decision block
if (x < 100) {
	
	console.log("x is less than 100!");
} else {
	
	console.log("x is greater than or equal to 100!")
} 


```

* NOTE: the IF statement expects a boolean, but if you pass it something that is not a boolean type coercion will occur.  

* NOTE2: JS defines a list of values that are considered "falsy"(values that return false when coerced to a boolean), these include values like 0 and "", anything else is automatically "truthy"

### Loops:

* JS has while, do/while, and for loops:

* break statements can be used to stop a loop.

```Javascript

// infinte while loop!

while (true) {
	
	console.log("Repeat!");
}

// Do/while loops always run at least once

var i = 0;

do {
	console.log("hello");
	i++;
} while (i < 10);


// for loop
for (var x = 0; x < 10; x++) {
	
	console.log(i);
}


```

### Functions

* Functions allow a way of calling code by a defined name


* NO PARAMATERS PASSED!

```Javascript

// No paramaters passed!
function printAmount() {
	
	console.log(amount.toFixed(2));
}

var amount = 99.99;


printAmount(); // "99.99"

amount = amount * 2;

printAmount(); // "199.98"

// Notice that the function is able to pull from the scope of the general program, but you can also pass variables as paramaters.
```

* PASSING W/ PARAMATERS!

```Javascript

// Passing w/ paramaters!
function printAmount(amt) {
	
	console.log(amt.toFixed(2));
}

function formatAmount() {
	
	return "$" + amount.toFixed(2);
}


var amount = 99.99;

printAmount(amount * 2); // 199.98

amount = formatAmount()
console.log(amount); // $99.99

```






