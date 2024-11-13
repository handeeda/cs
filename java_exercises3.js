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

nums=[4,2,6]
a=0
function all_even(listn){
    for (let i=0;i<listn.length;i=i+1){
        if (listn[i]%2==0){
            a=a+1
            if (a==3){
                console.log("all numbers are even")
            }
            else{
                console.log("all numbers are not even")
            }
        }
        
        
        
    }
}

all_even(nums);







