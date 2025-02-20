where = input("Go left or right? ")
counter = 0
while where == "right":
    counter += 1
    if counter > 2:
        print(":(")
    where = input("Go left or right? ")
print("You got out!")