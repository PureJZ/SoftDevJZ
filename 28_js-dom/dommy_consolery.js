// Team JZ :: Wen Zhang, Jackie Zeng 
// SoftDev pd5
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var 
//with parameter x
var f = function(x) 
{
    var j=30;  //Local variable that shadows the global variable 
    return j+x;
};


//instantiate an object
//objects can hold a variety of things (even functions!!)
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'}, //Object within an object (?)
          func : function(x) {  // A function !?!?!
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");   // Finds the list with id "thelist"
    var newitem = document.createElement("li");      // New item list
    newitem.innerHTML = text;
    list.appendChild(newitem);                       // Adds to the list with id "thelist"
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');  //Gets all list items
    listitems[n].remove();                                //Removes nth item
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');                      // Each li item now has the "red" class
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');                 //Even indexes will have the "red" class
	} else {
	    items[i].classList.add('blue');                //Odd indexes will have the "blue" class
	}
    }
};


//insert your implementations here for...
// FIB
let fib = function(n){
    if(n == 0){
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
}
// FAC
let fact = function(n){
    if (n == 1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}
// GCD

let gcd = function(a, b){
    var gcd
    for(i=0; i <= Math.min(a, b); i++){
        if(a%i==0 && b%i==0){
            gcd = i;
        }
    }
    return gcd
}

addItem("7th Fibonacci Number is: " + fib(7))
addItem("8!: " + fact(8))
addItem("GCD(104, 32) " + gcd(104, 32))


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {  // => does the same thing as writing function
    // body
    return retVal;
};