numa=[20,21,19,22,21,20,19,20,21,20]
list1=[]
let sum=0
function standard_deviation(nums1){
    n=nums1.length
    
    for (let i = 0; i < nums1.length; i++) {
        sum += nums1[i]
        
    }
    mean=sum/nums1.length
    for ( i = 0;i<nums1.length ;i=i+1){
        
        eachv=nums1[i]
        a=eachv-mean
        a=a**2
        a=a/n
        list1.push(a)


    }
    console.log(list1)
    for (let i = 0; i < list1.length; i++){
        sum += list1[i]
    }
    
}

standard_deviation(numa)