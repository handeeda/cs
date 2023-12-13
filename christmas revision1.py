"""
seconds1= int(input("write seconds"))
hours=seconds1/60
hours=hours/60
hours=int(hours)

minutes=seconds1/60
hours2=hours*60
minutes=minutes-hours2
minutes=int(minutes)

seconds1=seconds1-(hours*60*60+minutes*60)
seconds=seconds1

int3=int(seconds)
print(hours)
print(minutes)
print(seconds)


a=int(input("write the first variable for a"))
b=int(input("write the second variable for b"))

radius=int(input("write a radius of a circle"))

a=3
powerradius=pow(radius,2)
area=a*powerradius
circumference=2*radius*a
circumference=circumference*area
print("area is",area)
print("circumference is",circumference)


print("write the lengths")
a=int(input("write a"))
b=int(input("write b"))
c=int(input("write c"))
s=a+b+c
s=s/2
a=s-a
a=a*s
b=s-b
b=b*s
c=s-c
c=c*s
area=a+b+c
area=pow(area,2)
print(area)

principle=int(input("write the principle"))
rate=int(input("write the rate"))
time=int(input("write the time"))
ci=rate/100
ci=ci+1
ci=pow(ci,time)
ci=principle*ci
ci=ci-principle
print("compund interest is",ci)

"""










