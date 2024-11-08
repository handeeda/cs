let user={"name":"john doe","age":21};
let car={"engine_size":1200,"name":"mazda3"};
let a=0;
function can_drive_car(u,c){
    
    if (u["age"]>=18){
            a=a+1;
        }
    
    
    if (c["engine_size"]<=1000){
            a=a+1;
        }
    
    if (a==2){
        console.log("can drive a car!!");
    }
    else{
        console.log("cant drive a car....");
    }
 
}
can_drive_car(user,car);


function all_even(num1,num2,num3)


