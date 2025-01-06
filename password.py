import random
password=input("Enter the password:")
if(len(password)<8):
    print("password should have atleast 8 character ")
elif(random.search("[!@#$%^&*()]",password ) ):
    print("password should have atleast one special character")
elif(random.search("[a-z]",password)) and (random.search("[A-Z]",password)):
    print("password should have atleast 1 character")
else:
    print("valid password")
