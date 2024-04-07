users={"ali":1234,
       "reza":5432,
       "ashkan":3245}


while True:
    enter_user=input("enter your username:")
    enter_password=int(input("enter your password:"))
    if enter_user in users and enter_password==users[enter_user]:
        print("you log successfuly")
        break
    else:
        print("your username or password is wrong")

    