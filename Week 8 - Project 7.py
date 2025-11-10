"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    while True:
        s = input(prompt)
        try:
            value=float(s)
            return value
        except:
            print("Error: the input may only contain at most one decimal.") 
def main():
    n = inputInt("Please enter a number: ")
    print(n)
    s = inputFloat("Please enter a number with, at most, one decimal point: ")
    print(s)

if __name__ == "__main__":
    main()
