#write a python program to print simple interest
price =float (input("enter principle amount"))
rate =float(input("enter rate of interest"))
time= float(input("enter number of months"))
print("the given price is",price)
print("the given rate of interest is",rate)
print("the given time is",time)
omr = price * rate/100
print("the one month rate of interest is",omr)
totint=omr*time
print("the total interest is",totint)
tpa=totint*price
print("the total interest is",tpa)
