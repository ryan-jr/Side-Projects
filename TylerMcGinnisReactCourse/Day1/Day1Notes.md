# Tyler McGinnis React Course


* https://frontendmasters.com/books/front-end-handbook/2018/

### Why React/What is React?

* React is a library for building UIs

* Composition, unidirectional dataflow, explicit mutations, and clear JS make react special

* Composition is/are things like:

```
<SLider />
<Rouder />
<Navbar />
<Date />
<Map />
<Datepicker />
<Header />
<Carosel />
<Chart />
<Icon />
<SLider />

```

* React through components lets us build a larger app, through building a bunch of smaller apps e.g.:

```

<Containter>

		<Navbar />
		<Carousel />
		<Datepicker />

</Container>

```

* A component in React has 2 things that we need to think about: 

```
A.  State (What state will it handle/what stat will it need to get)
B.  What is the UI going to look at for this component?

```

* Function composition is applying one function to the result of another function:

```

function addStuff(x, y) {
	var z = x + y;
	return z;

}

function printStuff(x, y) {
	var a = addStuff(x, y);
	console.log(a);

}

printStuff(1, 2);

```


* In the above case we apply the function printStuff to the result of the function addStuff.  Having functions work together/depend on one another in order to return data in the right way/right format is function composition


* Unidirectional Data Flow:


```
For example with jQuery we set up event handlers that run and then update the DOM, but this can make things messy through updating state all over the place and not being well structured.

With React we still have event handlers, these handlers change the state, and then all of these things will update the UI.  React worries about updating the UI

Keep in mind state is data in your application

```

* Explicit Mutations

```
setState is used to set state of a component, and React takes care of everything else


```

* Javascript!

```
React is heavily based in/around JS and makes things easier that way

```


* Code!

```
<script>
console.log("hello");
// The HTML Version of what's going on below would look like:
// <h1 id="header">Ryan </h1>
var headerElement = React.createElement(
     "h1",
     { id: "header" },
     "Ryan"

     )

console.log(headerElement);
</script>

```


* We're building a react element first

* An element creates an object representation of a DOM node, for the element we pass in the tag we want to create as the first arg (as a string), then we pass in any attributes, and what we want it to hold


* Well how do we show the DOM node we've created to the user/screen/webpage?

* To do this we import the react-dom from the CDN and use:


```
ReactDOM.render(headerElement, 
document.getElementById("app"))

```

* What we're telling ReactDOM in the above code is what we want to render, and using vanilla JS, telling React where we want to render it to (the element with the id of "app")

* We know that we can create and render elements now what about adding variables/composing things?

* To do this we can wrap everything in a wrapper elment within the ReactDOM.render(), all the code that would go into that is below

```
var name = "Ryan";
var handle = "@rjr";

// The HTML Version of what's going on below would look like:
// <h1 id="header">Ryan </h1>
var headerElement = React.createElement(
     "h1",
     { id: "header" },
     "Ryan",
     name

     )

var nameElement = React.createElement (
     "h3",
     null,
     name
     )

var handleElement = React.createElement( 
     "h3",
     null,
     handle
     )

var wrapperElement = React.createElement("div", { id: "container"},
     nameElement, 
     handleElement
     )

console.log(headerElement);

          ReactDOM.render(wrapperElement, document.getElementById("app"))

```



* React keeps a virtual representation of the DOM

* The virtual DOM is just a class/object oriented representation of the DOM and React figures out how/when to update the DOM by comparing the "past" OO version of the DOM to the potential "new" OO version of the DOM e.g:

```
OldDOM === NewDOM

```

* If NewDom != OldDOM then it updates things, otherwise it stays the same.  

* The difference between a React element and a React component is that a React component is a function that optionally accepts input and returns a React element.  This means we could turn our elements into components by wrapping them in a function.  

* Input/data in React is known as props.  Props can access variables with props.VARIABLENAME

* To ensure that props/data is passed we have to have the function accept data/props and specify that the compoenent function is returning a React element.

```

function NameComponent (props) {
	return React.createElement(
		"h1",
		null,
		props.name,
	)

}

```

* To actually pass in those props/that data, we still use the wrapper element/React.createElement(s), in order to render the compoenent(s)(like the one above), and pass in the props/data that we want to use:

```

// This is incorrectly named handleElement even though it still passes in props
var handleElement = React.createElement( 
     "div",
     { id: "container" },
     React.createElement(NameComponent, { name: "Ryan" }),
     React.createElement(HandleComponent, { handle: "@rjr" }),
     )

```


* Ok, so all of this stuff with components, elements, etc... is confusing when all we want to do is make accessing/updating the UI easier...


```

function NameComponent (props) {
	return <h1>{props.name}</h1>
}

function HandleComponent (props) {
	return <h4>{props.handle}</h4>
}

function App() {
	return (
		<div id="container">

		<NameComponenet name="Ryan" />
		<HandleComponent handle="@rjr" />
		// Please note that with name and handle since they are already variables above we could write them out as name={ name } and handle={ handle } respectively.  


		</div>
	)

ReactDOM.render(
	<App />,
	Document.getElementById("app")
)
}