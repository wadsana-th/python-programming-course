"""
Number List Operations
Ask user to input 10 numbers and store them in a list
Display the original list
Create and display:
List of even numbers
List of odd numbers
List of numbers greater than the average
Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        number = int(input("Insert number [" + i +"]: "))
        numbers.append(number)
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = # Your code here
    odd_numbers = # Your code here
    
    # Calculate average
    average = # Your code here/ 10.0 # your code here
    
    # Numbers greater than average
    above_average = [] # Your code here
    for i in range(10):
        if numbers[1] % 2 == 0:
            even_numbers.append(numbers[1])
        else:
            odd_numbers.append(numbers[1])

        if numbers[1] > average:
            above_average.append(numbers[i])
                
   
    # Display results
    # Your code here
    print("Even Number List: ",  even_numbers)
    print("odd Number List: ",  odd_numbers)
    print("Above Average List:", above_average)
    print("Sum:", sum (numbers))
    print("Averge: ", average)
    print("Min: ", min(numbers))
    print("max: ", max(numbers))

if __name__ == "__main__":
    number_operations()