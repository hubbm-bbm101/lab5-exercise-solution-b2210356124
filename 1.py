N=int(input("Please enter a number greater than or equal to 1: "))
odd=0
even=0
for i in range (1,N+1,2):
    odd+=i
repetitions=0
for j in range (2,N+1,2):
    repetitions+=1
    even+=j
average=even/repetitions
if average==int(average)+0.0:
    average=int(average)
print(f"The sum of odd numbers is {odd} and the average of even numbers is {average}.")