number=5481
high=2026
low=0
count=0
guess=(high+low)//2
epsilon=0.01
while abs(guess*guess-number)>epsilon:
 count=count+1
 if guess*guess>number:
    high=guess-1
 else:
    low=guess+1
 guess=(high+low)/2
print("Times guessed:",count)
print("The square root of the number is:",guess)
 