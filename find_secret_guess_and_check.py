import secret_data
n=0
for i in range(0,2027):
    n=n+1
    if i==secret_data.secret_year:
        print("Times guessed:",n)
        print("Found year:",i)