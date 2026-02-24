# Simple program to check if a number is even or odd

def check_even_odd():
    # Take user input
    num = int(input("Enter a number: "))
    
    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

# Run the function
check_even_odd()