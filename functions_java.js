//for loops
//for (start value; conditional check; increment value)
for (let i = 0; i < 10; i=i+1){
    //if statement - for odd numbers
    if (i%2==1){
    console.log(i);
    console.log(i*2);
    }
    else if (i%2 ==0){
        console.log("even number found");

    }
    else{
        console.log("unknown number");
    }
}

function addTwoNumbers(number1,number2){
    let sum= number1+number2;
    return sum;
}
let answer = addTwoNumbers(5,7);
console.log(answer);