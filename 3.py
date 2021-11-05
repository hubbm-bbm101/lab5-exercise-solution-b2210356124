import random
largest=int(input("Please enter the largest number for the random number range: "))
chosen=random.randint(0,largest)
guesses=0
while True:
    user_choice=int(input("Please try to guess the random number: "))
    if user_choice<chosen:
        print("Try a larger number.")
        guesses+=1
    elif user_choice>chosen:
        print("Try a smaller number.")
        guesses+=1
    else:
        guesses+=1
        print(f"Congratulations, you found the right number in your {guesses}. guess.")
        break