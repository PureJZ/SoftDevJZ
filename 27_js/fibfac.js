//Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
let fact = function(n){
  if (n==1){
    return 1;
  }
  else {
    return
  }
}
//<your team's fact(n) implementation>

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)


//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
let fib = function(n){
  if (n ==0){
    return 0;
  }
    else if (n==1){
        return 1;}
    else {
    return (fib(n-1)+fib(n-2));
  }
}
//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

//=================================================================
