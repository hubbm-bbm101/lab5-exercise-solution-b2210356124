while True:
    mail=input("Please enter your e-mail: ")
    x=mail.count("@")
    y=mail.count(".")
    if x==1 and y==1 or x==1 and y>1:
        print("Your e-mail address is correct.")
        break
    else:
        print("Please enter a valid e-mail.")