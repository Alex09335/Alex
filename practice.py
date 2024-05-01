name=input("enter your name :")

def myfunction(name):
    ups=0
    lows=0
    for n in name:
        if n.isupper():
            ups=ups+1
        
        elif n.islower():
            lows=lows+1
           
        else:
            pass
    print(f"upper case is  {ups}")
    print(f"lows case is {lows}")
    
myfunction(name)        
     