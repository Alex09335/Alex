firstnumber=int(input("enter your first number:"))
secondnumber=int(input("enter your second number:"))
thirdnumber=int(input("enter your third number:"))

if firstnumber >secondnumber and secondnumber>thirdnumber:
    print(firstnumber,secondnumber,thirdnumber)
    
elif secondnumber>firstnumber and firstnumber>thirdnumber:
    print(secondnumber,firstnumber,thirdnumber)
elif secondnumber>firstnumber and thirdnumber>firstnumber:
    print(secondnumber,thirdnumber,firstnumber)
    
elif thirdnumber>firstnumber and firstnumber>secondnumber:
    print(thirdnumber,firstnumber,secondnumber)
elif thirdnumber>firstnumber and secondnumber>firstnumber:
    print(thirdnumber,secondnumber,firstnumber)    
else:
    print(" ")
    
              