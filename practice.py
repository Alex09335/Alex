def password_valid(password):
    if password_user.isalpha():
        print("your password must have at least 1 number")
    elif len(password_user)<8:
        print("your password must be 8 number and charechtor") 
    elif password_user.isnumeric():
        print("your password must have at least 1 charechtor")
    else:
        print("your password is correct")


while True:
    password_user=input("enter your password:")
    
    
    password_valid(password_user)