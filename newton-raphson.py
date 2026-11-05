from secret_data import secret_year
epsilon=0.01
guess=secret_year/2
count=0
while abs(guess**2-secret_year>epsilon):
    guess=guess-((guess**2-secret_year)/2*guess)
    count=count+1
print("Times guessed",count)
print("The result is:",guess)