startingPopulation = int(input("Enter the starting population: "))
growthRate = int(input("Enter the growth rate of the population: "))
growthHours = float(input("Enter the growth rate hours: "))
totalHours = float(input("Enter the total number of hours of growth: "))

startingHours = 0
while (growthHours <= totalHours):
    startingHours += growthHours
    if startingHours <= totalHours:
        startingPopulation *= growthRate
    else:
        break


print("The ending population will be: ", startingPopulation, "organisms.")
