//objects/dictionaries in JS 
let my_object={"a":1,"b":2,"c":3};
console.log(my_object);
//to loop through the keys for ....in loop
for (key in my_object){
    console.log(key,my_object[key]);
}
//to return a list of keys
let my_keys=Object.keys(my_object);
console.log(my_keys);
//to return a list of values
let my_values= Object.values(my_object);
//to return a list of key,value pairs
let my_kv_pairs= Object.entries(my_object);
console.log(my_kv_pairs);

//the forEach method can be used with an array
//it passes every value in the array into a
//function- kind of like map() in python
function double_values(value_in){
    console.log(value_in*2);
}

my_values.forEach(double_values);
//for .... of will loop through each
//value in an array
for (let v of my_values){
    console.log(v);
} 
//to make a object (read dictionary) from
// a list
let my_dictionary=Object.fromEntries(my_kv_pairs);
