Registration=dict()
while True:
    print("1:Register\n2:Login\n3:Display Details\n4:Logout")
    user_input=int(input("Choose one option from the above list:"))
    if user_input==1:
        print("Register")
        user_name=input("Enter Your Name:")
        email=input("Enter email:")
        roll_no=int(input("Enter your RollNo:"))
        password=input("Enter the password:")
        if roll_no not in Registration.keys():
            Registration[roll_no]=[user_name,email,password]
            print("Registration Successfull")
        else:
             print("User name already exists") 
    elif user_input==2:
        print("Login")
        roll=int(input("Enter registerd RollNo:"))
        pswd=input("Enter password:")
        if roll not in Registration.keys():
            print("User not found")
        elif pswd!=Registration[roll_no][2]:
            print("Invalid password")
        else:
            print("Login Successfull")
    elif user_input==3:
        print("Details of the User")
        print(Registration)
    else:
        print("Logged out successfully")
        break
    
