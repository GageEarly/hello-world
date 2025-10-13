dropHeight = float(input("Enter how high you will drop the ball in feet: "))
bounceIndex = float(input("Enter the bounce index in feet: "))
bounceLimit = int(input("Enter the number of times you want the ball to bounce: "))

distance = dropHeight

for i in range(bounceLimit):
    dropHeight *= bounceIndex
    distance += dropHeight * 2

print("The total distance the ball traveled is ", distance, " feet.")
