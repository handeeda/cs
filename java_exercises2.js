for (let i=0; i<=20;i=i+1){
    console.log(i);
}

for (i=3; i<=29;i=i+1){
    if (i%2==1){
    console.log(i);
    }

    else{
        continue;
    }
}

for(i=12; i>=-14;i=i-1){
    if(i%2==0){
        console.log(i);

    }
    else{
        continue;
    }
}

for (i=50;i>=20;i=i-1){
    if (i%3==0){
        console.log(i);
    }
    else{
        continue;
    }
}

i=-13
if(i>0){
    console.log("this is a positive number")
}
else if(i<0){
    console.log("this is a negative number")
}

i=6
if(i%2==0){
    console.log("this is a even number")
}
else{
    console.log("this is a odd number")
}


a=7
b=7
if (a>b){
    console.log(a,"is greater than",b)
}
else if(b>a){
    console.log(b,"is greater than",a)
}
else{
    console.log("they are equal")
}

let grade=10
if (grade==10){
    console.log("A")
}
if (grade==9){
    console.log("B")
}
if (grade==8){
    console.log("C")
}
if (grade==7){
    console.log("D")
}
if (grade==6){
    console.log("E")
}
if (grade<=5){
    console.log("F")
}

let age=25
if (age<=12){
    console.log("ticket price is 5")
}
if (age<=18 && age>12){
    console.log("ticket price is 10")
}
if (age<=60 && age>18){
    console.log("ticket price is 20")
}
if (age>60){
    console.log("ticket price is 15")
}


function minutes_to_hours(a){
    a=a/60;
    return a;
}
let answer= minutes_to_hours(120);
console.log(answer,"hours");

function average_of_4_numbers(a,b,c,d){
    sum=a+b+c+d;
    sum=sum/4;
    return sum;
}
answer=average_of_4_numbers(3,13,4,6);
console.log(answer);

function get_gasoline_amount(kilo,litre){
    kilo=kilo*2;
    litre=kilo/litre;
    return litre;
}
answer=get_gasoline_amount(500,750);
    console.log(answer);