
numa=[20,21,19,22,21,20,19,20,21,20]
numb=[303,299,306,298,304,307,299,302,305,299,300]
numc=[15.3,14.9,15.1,15.2,14.8,14.7,15.1,14.8,15.0,15.0]
numd=[87,89,84,88,89,87,86,87,86,87]
list1=[]
let sum=0
function standard_deviation(nums1){
    n=nums1.length
    
    for (let i = 0; i < nums1.length; i++) {
        sum += nums1[i]
        
    }
    mean=sum/nums1.length
    console.log("mean:",mean)
    for ( i = 0;i<nums1.length ;i=i+1){
        
        eachv=nums1[i]
        a=eachv-mean
        a=a**2
        list1.push(a)


    }
    //console.log(list1)
    sum=0
    for ( i = 0; i < list1.length; i++){

        sum += list1[i]

        


    }
    sum=sum/(n-1)
    answer=Math.sqrt(sum)
    console.log("standard deviation",answer)
    
}

standard_deviation(numa)
standard_deviation(numb)
standard_deviation(numc)
standard_deviation(numd)