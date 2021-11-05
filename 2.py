while True:
    mail=input("Please enter your e-mail: ")
    x=0 #counter for @
    y=0 #counter for .
    for i in range (0,len(mail)):
        if mail[i]=="@":
            x+=1
    for j in range (0,len(mail)):
        if mail[j]==".":
            y+=1
    if x == 1 and y >= 1:
        print("Your e-mail address is correct.")
        break
    else:
        print("Please enter a valid e-mail.")
