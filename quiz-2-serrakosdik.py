cube=input("Enter a positive integer:")
cube=int(cube)
for guess in range(0,cube+1):
 if guess**3==cube:
    print("Cube root of",cube,"is",guess)
    break
else:
    print(cube,"is not a perfect cube")